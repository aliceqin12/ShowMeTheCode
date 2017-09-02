import os
import glob
from PIL import Image

def resize_image(max_width, max_height, filepath):
    """
    :param max_width:
    :param max_length:
    :param filename: 图片路径
    :return:
    """
    if os.path.exists(filepath):
        pics = glob.glob(r'*.jpg')
        for pic in pics:
            image = Image.open(pic)
            (x, y) = image.size
            changex = float(x) / max_width
            changey = float(y) / max_height

            if changex > 1.0 or changey > 1.0:
                change = changex if changex > changey else changey
                image.resize((int(x/change), int(y/change))).save(pic)

def main():
    max_width = 640
    max_height = 1136
    filepath = '/'
    resize_image(max_width, max_height, filepath)

if __name__ == '__main__':
    main()