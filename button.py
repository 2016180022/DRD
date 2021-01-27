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
		
	def update(self):
		pass

	def draw(self):
		pass

	def handle_event(self, e):
		pair = (e.type, e.button)
		x, y = e.x, e.y
		#if self.mouse_point is None:
		if pair == LBTN_DOWN:
			if gobj.pt_in_rect(gobj.set_mouse_pos(x, y, 1), self.get_bb()):
				return True
			if e.type == SDL_MOUSEMOTION:
				self.mpos = set_mouse_pos(x, y, 1)
				if gobj.pt_in_rect(mpos, self.get_bb()):
					return True
				else:
					return False
			return False

		if pair == LBTN_UP:
			mpos = gobj.set_mouse_pos(x, y, 1)
			if gobj.pt_in_rect(gobj.set_mouse_pos(x, y, 1), self.get_bb()):
				if gobj.pt_in_rect(self.mpos, self.get_bb()):
					self.callback()
					return False

	def get_bb(self):
		return self.x - self.w // 2, self.y - self.h // 2, self.x + self.w // 2, self.y + self.h // 2