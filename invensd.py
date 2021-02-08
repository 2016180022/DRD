#start at 210208
from pico2d import *
import gfw
import gobj

SD_DIR = gobj.RES_DIR + 'invensd/'

class Invensd:
	def __init__(self, x, y, sdchar):
		self.x, self.y, self.char = x, y, sdchar

	def update(self):
		pass

	def draw(self):
		image = gfw.image.load(SD_DIR + self.char + '.png')
		image.draw(self.x, self.y, 1.5 * image.w, 1.5 * image.h)

	def handle_event(e, self):
		pass

	def get_bb(self):
		width = 40
		height = 45
		x, y = self.x, self.y
		return x - width, y - height, x + width, y + height