

def hex_to_rgb(hex:str):
    if len(hex) != 6 and len(hex) != 7:
        print(len(hex))
        return None
    else:
        hex = hex.lstrip("#")
        rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        return rgb
    
def rgb_to_hex(rgb:tuple):
    if len(rgb) != 3:
        print(len(hex))
        return None
    else:
        hex = "#%02x%02x%02x" % rgb
        return hex




