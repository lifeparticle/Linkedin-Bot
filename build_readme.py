from datetime import datetime as date
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

def load_bg_image(image_name):
	return Image.open(image_name)

def output_final_image(output_image_name, bg_image):
	draw = ImageDraw.Draw(bg_image)
	bg_width, bg_height = bg_image.size

	font = ImageFont.truetype("Roboto-Light.ttf", 16)
	text = date.today().strftime("%A")
	width, height = font.getsize(text)

	x = (bg_width - width) / 2
	y = (bg_height - height) / 2
	padding = 10

	draw.rectangle((x - padding, y - padding, x + width + padding, y + height + padding), outline = None, fill = 'black')
	draw.text((x, y), text, (255, 255, 255), font = font)

	bg_image.save(output_image_name)

if __name__ == "__main__":
	bg_image = load_bg_image("bg.png")
	output_final_image("output.png", bg_image)