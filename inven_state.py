#start at 210111
from pico2d import *
import gfw
import gobj

inven = 'demo'

canvas_width = 720
canvas_height = 480

def enter():
	gfw.world.init(['bg', 'isd'])

	bg = gobj.ImageObject('inven_item.png', canvas_width // 2, canvas_height // 2, canvas_width, canvas_height)
	gfw.world.add(gfw.layer.bg, bg)

def update():
	gfw.world.update()

def draw():
	gfw.world.draw()

def handle_event(e):
	if e.type == SDL_QUIT:
		return gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			return gfw.pop()

def exit():
	pass