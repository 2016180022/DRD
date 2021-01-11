#start at 210106

import gfw
import gobj
from pico2d import *
from sd import SD

CANVAS_WIDTH = 720
CANVAS_HEIGHT = 480

def enter():
	global sd
	gfw.world.init(['bg', 'sd', 'mob'])
	sd = SD()
	gfw.world.add(gfw.layer.sd, sd)

	bg = gobj.ImageObject('demotile_town.png', CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, CANVAS_WIDTH, CANVAS_HEIGHT)
	gfw.world.add(gfw.layer.bg, bg)

def update():
	gfw.world.update()

def draw():
	gfw.world.draw()

def handle_event(e):
	global sd
	if e.type == SDL_QUIT:
		gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			gfw.pop()

	sd.handle_event(e)


def exit():
	pass

if __name__ == '__main__':
	gfw.run_main()