from PIL import Image
from importlib import resources
from io import BytesIO
from functools import lru_cache

from .image_pixelifier import pixelify_image
from .block_to_color import *


@lru_cache(maxsize=256)
def _load_block_texture(blocks_dir: str, block_name: str) -> Image.Image:
    # Cache PNGs so we don't reopen them thousands of times.
    with resources.files("image_to_minecraft.blocks").joinpath(block_name).open("rb") as f:
        im = Image.open(f).convert("RGB")
    # Copy into memory so the file handle can close cleanly
    return im.copy()

def converter_path(
        image_path: str,
        width: int = 128, 
        blocks_dir:str = "blocks", 
        blocks_json: str = "blocks.json",
        tile_size: int = 16
    ) -> Image.Image:
    d = load_palette(blocks_json)

    im = Image.open(image_path)
    im = im.convert("RGB")
    img = pixelify_image(im, width)
    pix = img.load()

    new_im = Image.new('RGB', (img.width * tile_size, img.height * tile_size))
    y_offset = 0
    for row in range(img.height):
        x_offset = 0
        row_im = Image.new("RGB", (img.width * tile_size, tile_size))
        for col in range(img.width):
            cc = pix[col, row]
            print(cc)
            p_block = find_closest_color_in_json(color= cc, palette_items=d)
            block_im = _load_block_texture(blocks_dir, p_block)
            row_im.paste(block_im, (x_offset, 0))
            x_offset += tile_size
        
        new_im.paste(row_im, (0, y_offset))
        y_offset += tile_size
    
    #new_im.save("image.png")
    return new_im

                
def converter_bytes(
        image_bytes: bytes,
        width: int = 128, 
        blocks_dir:str = "blocks", 
        blocks_json: str = "blocks.json",
        tile_size: int = 16
    ) -> Image.Image:
    d = load_palette(blocks_json)

    # Load image from bytes
    with Image.open(BytesIO(image_bytes)) as input_img:
        input_img = input_img.convert("RGB")

        # pixelify_image must accept a PIL Image
        img = pixelify_image(input_img, width)
    pix = img.load()

    new_im = Image.new('RGB', (img.width * tile_size, img.height * tile_size))
    y_offset = 0
    color_cache = {}
    for row in range(img.height):
        x_offset = 0

        row_im = Image.new("RGB", (img.width * tile_size, tile_size))

        for col in range(img.width):
            cc = pix[col, row]
            print(cc)
            block_name = color_cache.get(cc)
            if block_name == None:
                block_name = find_closest_color_in_json(color= cc, palette_items=d)
                color_cache[cc] = block_name

            block_im = _load_block_texture(blocks_dir, block_name)
            row_im.paste(block_im, (x_offset, 0))
            x_offset += tile_size
        
        new_im.paste(row_im, (0, y_offset))
        y_offset += tile_size
    
    #new_im.save("image.png")
    return new_im