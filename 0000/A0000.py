from PIL import Image, ImageFont, ImageDraw

def make_txt(width, height):
    txt = Image.new("RGBA", (width, height), (255, 255,255, 0))
    font = ImageFont.truetype('FUTURA_3.TTF', size=int(width*0.2))
    draw = ImageDraw.Draw(txt)
    draw.text((int(width*0.9),0), '1', font=font, fill=(255,0,0,255))
    return txt

def main():
    image = Image.open('2.jpg').convert('RGBA')
    (w, h) = image.size
    txt = make_txt(w, h)

    out = Image.alpha_composite(image,txt)
    out.show()

if __name__ == '__main__':
    main()