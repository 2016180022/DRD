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

stage = 'demo'

STATE_PLAYING, STATE_PAUSED = range(2)

def enter():
	gfw.world.init(['bg', 'sd', 'mob'])

	fn = 'tile_' + stage + '.png'
	bg = gobj.ImageObject(fn, canvas_width // 2, canvas_height // 2, canvas_width, canvas_height)
	gfw.world.add(gfw.layer.bg, bg)

	life_gauge.load()
	mg.init()

	global game_state
	game_state = STATE_PLAYING

	global pause_image
	pause_image = gfw.image.load(gobj.RES_DIR + 'pause_demo.png')

def pause_game():
	global game_state
	game_state = STATE_PAUSED
	print('paused game')

def resume_game():
	global game_state
	game_state = STATE_PLAYING
	print('resume game')

def update():
	global game_state

	if game_state != STATE_PLAYING:
		return

	gfw.world.update()
	# if mg.generate_mob():
	# 	mg.generate_mob()
	# if gfw.world.count_at(gfw.layer.sd) > 0 and gfw.world.count_at(gfw.layer.mob) > 0:
	# 	attack_mob()

def draw():
	gfw.world.draw()
	gobj.draw_collision_box()
	if game_state == STATE_PAUSED:
		x = get_canvas_width() // 2
		y = get_canvas_height() // 2
		pause_image.draw(x, y)

def handle_event(e):
	if e.type == SDL_QUIT:
		return gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			if game_state != STATE_PAUSED:
				pause_game()
			else:
				return gfw.pop()
		elif e.key == SDLK_RETURN:
			if game_state == STATE_PAUSED:
				resume_game()
		elif e.key == SDLK_c:
			set_sd()
		elif e.key == SDLK_v:
			set_mob()
		elif e.key == SDLK_b:
			mob.decrease_life(10)

	# if gfw.world.objects_at(gfw.layer.sd):
	# 	sd.handle_event(e)
	for obj in gfw.world.objects_at(gfw.layer.sd):
		if obj.handle_event(e):
			pass
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