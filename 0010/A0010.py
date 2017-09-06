from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string

Letters = 'abcdefghkmnprstuvwxyzABCDEFGHKMNPRSTUVWXYZ'

def randLetter():
    return random.choice(Letters)

def randColor():
    return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

def compose():
    width = 240
    height = 60

    image = Image.new('RGBA', (width,height))
    # fill different color in different pixel
    for i in range(width):
        for j in range(height):
            image.putpixel((i, j), randColor())

    # write letter
    font = ImageFont.truetype('FUTURA_3.TTF', int(width * 0.25))
    draw = ImageDraw.Draw(image)
    draw.text((20, 0), randLetter(), font=font, fill=randColor())
    draw.text((80, 0), randLetter(), font=font, fill=randColor())
    draw.text((140, 0), randLetter(), font=font, fill=randColor())
    draw.text((200, 0), randLetter(), font=font, fill=randColor())

    # blur image
    image = image.filter(ImageFilter.BLUR)

    return image

if __name__ == '__main__':
    image = compose()
    image.show()