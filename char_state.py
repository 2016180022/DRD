#start at 210205
from pico2d import *
import gfw
import gobj
from button import Button

canvas_width = 720
canvas_height = 480

def enter():
	gfw.world.init(['bg'])

	bg = gobj.ImageObject('inven_char_demo.png', canvas_width // 2, canvas_height // 2, canvas_width, canvas_height)
	gfw.world.add(gfw.layer.bg, bg)

def exit():
	pass

def handle_event(e):
	if e.type == SDL_QUIT:
		return gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			return gfw.pop()

def update():
	gfw.world.update()

def draw():
	gfw.world.draw()