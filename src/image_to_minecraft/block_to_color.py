from PIL import Image
import os
import json
import math

def block_to_color(image_path): #for now doesn't work with goofy dimensions
    try:
        im = Image.open(image_path)
        pix = im.load()
        rgb = (0, 0, 0)
        for row in range(im.height):
            for col in range(im.width):
                nc = pix[col, row]
                rgb = tuple(rgb[i] + nc[i] for i in range(3))

        rgb = tuple(x // (im.width*im.height) for x in rgb)
        return rgb
    except TypeError as e:
        print(e)
        print("total color, new color:", rgb, nc)
    except IndexError as e:
        print(e)
        print(image_path)
        print("row+col:",row, col)
        print("image dimensions:", im.height, im.width)

def folder_to_colors(folder_path: str):
    colors = {}
    with os.scandir(folder_path) as d:
        for e in d:
            if os.path.splitext(e)[1] in [".png", ".jpg", ".jpeg"]:
                color = block_to_color(e.path)
                colors[e.name] = color

    return colors

def jsonify(dict):
    with open("blocks.json", "w") as file:
        json.dump(dict, file, indent=4)

#jsonify(folder_to_colors("blocks_filtered"))
        
def find_closest_color_in_json(color: tuple, blocks_list: dict):
    # filters
    if len(color) != 3:
        return None
    # good part
    current_best = ""
    best_delta = 765
    for k, v in blocks_list.items():
        if v:
            delta = math.sqrt((v[0] - color[0])**2 + (v[1] - color[1])**2 + (v[2] - color[2])**2)
            if delta < best_delta:
                best_delta = delta
                current_best = k

    return current_best

block = find_closest_color_in_json((29, 155, 209))
"""
print(block)
with open("blocks.json", "r", encoding='utf-8') as file:
    s = file.read()
    d = json.loads(s)
print("block color:", d[block])
"""