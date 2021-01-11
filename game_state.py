#start at 210106

import gfw
import gobj
from pico2d import *
from sd import SD

CANVAS_WIDTH = 720
CANVAS_HEIGHT = 480

def enter():
	gfw.world.init(['bg', 'sd', 'mob'])

	bg = gobj.ImageObject('demotile_town.png', CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, CANVAS_WIDTH, CANVAS_HEIGHT)
	gfw.world.add(gfw.layer.bg, bg)

def update():
	gfw.world.update()

def draw():
	gfw.world.draw()

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			gfw.pop()
		elif e.key == SDLK_c:
			set_sd()
			print("set mod")

	if gfw.world.count_at(gfw.layer.sd) > 0:
		sd.handle_event(e)
	else:
		return

def exit():
	pass

def set_sd():
	global sd
	sd = SD()
	gfw.world.add(gfw.layer.sd, sd)
	print("set sd")

if __name__ == '__main__':
	gfw.run_main()