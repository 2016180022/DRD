#start at 210106

import gfw
import gobj
from pico2d import *
from sd import SD
from mob import Mob
import life_gauge
import mob_generator as mg

canvas_width = 720
canvas_height = 480

def enter():
	gfw.world.init(['bg', 'sd', 'mob'])

	bg = gobj.ImageObject('demotile_town.png', canvas_width // 2, canvas_height // 2, canvas_width, canvas_height)
	gfw.world.add(gfw.layer.bg, bg)

	life_gauge.load()
	mg.init()

def update():
	gfw.world.update()
	# if mg.generate_mob():
	# 	mg.generate_mob()
	# if gfw.world.count_at(gfw.layer.sd) > 0 and gfw.world.count_at(gfw.layer.mob) > 0:
	# 	attack_mob()

def draw():
	gfw.world.draw()
	gobj.draw_collision_box()

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
		elif e.key == SDLK_b:
			mob.decrease_life(10)

	if gfw.world.count_at(gfw.layer.sd) > 0:
		sd.handle_event(e)
		# for s in gfw.world.objects_at(gfw.layer.sd):
		# 	if gobj.collides_box(sd, s):
		# 		print('cannot place there', sd)
		# 		return
	else:
		return

def exit():
	pass

def attack_mob():
	if sd.attack_target():
		mob.decrease_life(50)

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