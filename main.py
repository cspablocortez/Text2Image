# Text2Image
from PIL import Image as PIL_Image
from PIL import ImageDraw, ImageFont
from poems import poems


class Text:
	def __init__(self, text, author, index):
		self.text = text
		self.author = author
		self.index = index

	def render(self):
		image = Image(self.text, self.author, self.index)
		image.render()
		

class Image:
	def __init__(self, text, author, index):
		self.width = 600
		self.height = 800
		self.dimensions = (self.width, self.height)
		self.background_color = (247, 242, 231)
		self.xy = (100, 0)
		self.text = text
		self.author = author
		self.fill = (0, 0, 0)
		self.font = ImageFont.truetype("Open_Sans/OpenSans-Regular.ttf", 15)
		self.author_font = ImageFont.truetype("Open_Sans/OpenSans-Italic.ttf", 10)
		self.spacing = 10
		self.align = "left"
		self.index = index


	def render(self):
		image = PIL_Image.new('RGB', self.dimensions, self.background_color)
		draw = ImageDraw.Draw(image)
		draw.multiline_text(self.xy, self.text, fill=self.fill, font=self.font, anchor=None, spacing=self.spacing, align=self.align)
		draw.multiline_text((450, 750), self.author, fill=self.fill, font=self.author_font, anchor=None, spacing=self.spacing, align="right")
		image.save("image" + str(self.index) + ".png", "PNG")
		del draw



for index, poem in enumerate(poems, start=1):
	poem = Text(poem, "Roberto Bolaño", index)
	poem.render()



