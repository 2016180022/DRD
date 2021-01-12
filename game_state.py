#start at 210106

import gfw
import gobj
from pico2d import *
from sd import SD
from mob import Mob

canvas_width = 720
canvas_height = 480

def enter():
	gfw.world.init(['bg', 'sd', 'mob'])

	bg = gobj.ImageObject('demotile_town.png', canvas_width // 2, canvas_height // 2, canvas_width, canvas_height)
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
		elif e.key == SDLK_v:
			set_mob()


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

def set_mob():
	global mob
	mob = Mob()
	gfw.world.add(gfw.layer.mob, mob)
	print("set mob")

if __name__ == '__main__':
	gfw.run_main()