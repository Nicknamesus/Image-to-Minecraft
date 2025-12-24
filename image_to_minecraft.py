import os
from PIL import Image
from image_pixelifier import pixelify_image
from block_to_color import *

def image_to_minecraft(image_path: str, width: int = 128, blocks_folder: str = "blocks.json"):
    img = pixelify_image(image_path, width)
    pix = img.load()

    for row in range(img.height - 1):
            for col in range(img.width - 1):
                cc = pix[row, col]
                p_block = find_closest_color_in_json(color= cc, )
                print(p_block)

image_to_minecraft("rose.jpg")