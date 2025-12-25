import os
from PIL import Image
from image_pixelifier import pixelify_image
from block_to_color import *

def image_to_minecraft(image_path: str, width: int = 128, blocks_folder: str = "blocks.json"):
    img = pixelify_image(image_path, width)
    pix = img.load()

    new_im = Image.new('RGB', (img.width * 16, img.height * 16))
    y_offset = 0
    for row in range(img.height):
        x_offset = 0
        row_im = Image.new("RGB", (img.width * 16, 16))
        for col in range(img.width):
            cc = pix[col, row]
            print(cc)
            p_block = find_closest_color_in_json(color= cc)
            block_im = Image.open(f"InventivetalentDev 1.19.3 blocks/{p_block}")
            row_im.paste(block_im, (x_offset, 0))
            x_offset += 16
        
        new_im.paste(row_im, (0, y_offset))
        y_offset += 16
        
    new_im.save("image.png")

                

image_to_minecraft("bender.jpeg", width= 124)