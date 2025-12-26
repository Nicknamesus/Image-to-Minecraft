from PIL import Image

def pixelify_image(image_path, new_width):
    im = Image.open(image_path)
    w_ratio = new_width / im.width

    resized_img = im.resize((new_width, round(im.height*w_ratio)), Image.Resampling.LANCZOS)
    return resized_img
