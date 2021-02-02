#start at 210127
from pico2d import *
import gobj
import gfw

LBTN_DOWN = (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)
LBTN_UP = (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT)

class Button:
	def __init__(self, x, y, w, h, callback):
		self.x, self.y, self.w, self.h = x, y, w, h
		self.callback = callback
		self.mpos = (0, 0)
		self.capture = False
		self.mouse_point = None
		
	def update(self):
		pass

	def draw(self):
		pass

	def handle_event(self, e):
		pair = (e.type, e.button)
		x, y = e.x, e.y
		if self.mouse_point is None:
			if pair == LBTN_DOWN:
				if gobj.pt_in_rect(gobj.set_mouse_pos(x, y, 1), self.get_bb()):
					self.capture = True
					self.mouse_point = gobj.set_mouse_pos(x, y, 1)
					return True
			if e.type == SDL_MOUSEMOTION:
				self.mpos = gobj.set_mouse_pos(x, y, 1)
				if gobj.pt_in_rect(self.mpos, self.get_bb()):
					self.capture = True
					return True
				else:
					self.capture = False
					return False
			return False

		if pair == LBTN_UP:
			self.capture = False
			self.mouse_point = None
			#mpos = gobj.set_mouse_pos(x, y, 1)
			if gobj.pt_in_rect(gobj.set_mouse_pos(x, y, 1), self.get_bb()):
				self.callback()
				return False

		if e.type == SDL_MOUSEMOTION:
			if gobj.pt_in_rect(gobj.set_mouse_pos(x, y, 1), self.get_bb()):
				self.capture = True
			else:
				self.capture = False

	def get_bb(self):
		return self.x - self.w // 2, self.y - self.h // 2, self.x + self.w // 2, self.y + self.h // 2

	def print_capture(self):
		if self.capture == True:
			print("capture")
		else:
			print("non-captured")