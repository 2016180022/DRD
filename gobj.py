# import random
from pico2d import *
import gfw

RES_DIR = './res/'

def point_add(point1, point2):
	x1,y1 = point1
	x2,y2 = point2
	return x1+x2, y1+y2

def move_obj(obj):
	obj.pos = point_add(obj.pos, obj.delta)

def move_draw_obj(obj):
	obj.draw_pos = point_add(obj.draw_pos, obj.delta)

def collides_box(a,b):
	(la, ba, ra, ta) = a.get_bb()
	(lb, bb, rb, tb) = b.get_bb()

	if la > rb: return False
	if ra < lb: return False
	if ba > tb: return False
	if ta < bb: return False

	return True

def draw_collision_box():
	for obj in gfw.world.all_objects():
		if hasattr(obj, 'get_bb'):
			draw_rectangle(*obj.get_bb())

def set_mouse_pos(pos_x, pos_y, repos=None):
	px, py = pos_x, get_canvas_height() - pos_y - 1
	x, y = px, py
	if repos == None:
		x += 100
		y += 100
	return x, y

def pt_in_rect(point, rect):
	(x, y) = point
	(l, b, r, t) = rect

	if x < l : return False
	if x > r: return False
	if y < b: return False
	if y > t: return False

	return True

def set_flip_pos(pos_x, pos_y):
	x, y = pos_x, pos_y
	x += 62
	#y -= 67
	return x, y

def set_pos_origin(pos_x, pos_y):
	x, y = pos_x, pos_y
	x -= 62
	y += 67
	return x, y

def set_sd_pevot(pos_x, pos_y):
	x, y = pos_x, pos_y
	x -= x % 60
	y -= y % 60
	return x, y

class ImageObject:
	def __init__(self, imageName, x, y, x2, y2):
		self.image = gfw.image.load(RES_DIR + imageName)
		self.x, self.y = x, y
		self.x2, self.y2 = x2, y2
	def draw(self):
		self.image.draw(self.x, self.y, self.x2, self.y2)
	def update(self):
		pass

if __name__ == "__main__":
	print("This file is not supposed to be executed directly.")
