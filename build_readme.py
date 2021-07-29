from datetime import datetime as date
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
import numpy as np

if __name__ == "__main__":
	img = Image.open("bg.png")
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("Roboto-Light.ttf", 16)
	draw.rectangle((530, 80, 640, 130), outline = None, fill = 'black')
	draw.text((550, 95), date.today().strftime("%A"), (255, 255, 255), font = font)
	img.save('output.png')