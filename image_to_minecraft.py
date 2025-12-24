import os
from PIL import Image
from image_to_minecraft import pixelify_image

def image_to_minecarft(image_path: str, width: int = 128, blocks_folder: str = "blocks.json"):
    img = pixelify_image(image_path, width)
    