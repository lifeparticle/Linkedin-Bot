from datetime import datetime as date
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

def load_bg_image(image_name):
	return Image.open(image_name)

def output_final_image(output_image_name, bg_image):
	draw = ImageDraw.Draw(bg_image)
	font = ImageFont.truetype("Roboto-Light.ttf", 16)
	draw.rectangle((530, 80, 640, 130), outline = None, fill = 'black')
	draw.text((550, 95), date.today().strftime("%A"), (255, 255, 255), font = font)
	bg_image.save(output_image_name)

if __name__ == "__main__":
	bg_image = load_bg_image("bg.png")
	output_final_image("output.png", bg_image)