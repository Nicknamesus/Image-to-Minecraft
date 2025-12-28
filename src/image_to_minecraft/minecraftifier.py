from PIL import Image
from .image_pixelifier import pixelify_image
from .block_to_color import *
from io import BytesIO

def converter_path(image_path: str, width: int = 128, blocks_list: str = "blocks.json"):
    im = Image.open(image_path)
    im = im.convert("RGB")
    img = pixelify_image(im, width)
    pix = img.load()

    new_im = Image.new('RGB', (img.width * 16, img.height * 16))
    y_offset = 0
    for row in range(img.height):
        x_offset = 0
        row_im = Image.new("RGB", (img.width * 16, 16))
        for col in range(img.width):
            cc = pix[col, row]
            print(cc)
            p_block = find_closest_color_in_json(color= cc, filepath=blocks_list)
            block_im = Image.open(f"blocks/{p_block}")
            row_im.paste(block_im, (x_offset, 0))
            x_offset += 16
        
        new_im.paste(row_im, (0, y_offset))
        y_offset += 16
    
    #new_im.save("image.png")
    return new_im

                
def converter_bytes(image_bytes: bytes, width: int = 128, blocks_list: str = "blocks.json"):
    try:
        with open(blocks_list, "r", encoding='utf-8') as file:
            s = file.read()
            d = json.loads(s)
    except Exception as e:
        print(e)
        return None

    # Load image from bytes
    with Image.open(BytesIO(image_bytes)) as input_img:
        input_img = input_img.convert("RGB")

        # pixelify_image must accept a PIL Image
        img = pixelify_image(input_img, width)
    pix = img.load()

    new_im = Image.new('RGB', (img.width * 16, img.height * 16))
    y_offset = 0
    for row in range(img.height):
        x_offset = 0
        row_im = Image.new("RGB", (img.width * 16, 16))
        for col in range(img.width):
            cc = pix[col, row]
            print(cc)
            p_block = find_closest_color_in_json(color= cc, blocks_list=d)
            block_im = Image.open(f"blocks/{p_block}")
            row_im.paste(block_im, (x_offset, 0))
            x_offset += 16
        
        new_im.paste(row_im, (0, y_offset))
        y_offset += 16
    
    #new_im.save("image.png")
    return new_im