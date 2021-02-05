#start at 210106
import gfw
import gobj
from pico2d import *
from sd import SD
from mob import Mob
from button import Button
import life_gauge
import mob_generator as mg
import inven_state
import char_state

canvas_width = 720
canvas_height = 480
ui_margin = 30
ui_x, ui_y = 645, 465
ui_w, ui_h = 150, 30

index = 0
WAVE = 20

stage = 'demo'

STATE_PLAYING, STATE_PAUSED = range(2)

def start(inven):
	if inven == 'inven':
		gfw.push(inven_state)
	elif inven == 'char':
		gfw.push(char_state)
	elif inven == 'menu':
		print('menu tab in/out not apply')

def create_state():
	gfw.world.init(['bg', 'sd', 'mob', 'ui'])

	fn = 'tile_' + stage + '.png'
	bg = gobj.ImageObject(fn, canvas_width // 2, canvas_height // 2, canvas_width, canvas_height)
	gfw.world.add(gfw.layer.bg, bg)

	life_gauge.load()
	mg.init()

	set_menu()

	global game_state
	game_state = STATE_PLAYING

def enter():
	create_state()
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
	draw_menu()
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
			mob.decrease_life(10, 1)

	# if gfw.world.objects_at(gfw.layer.sd):
	# 	sd.handle_event(e)
	for obj in gfw.world.objects_at(gfw.layer.sd):
		if obj.handle_event(e):
			pass
		# for s in gfw.world.objects_at(gfw.layer.sd):
		# 	if gobj.collides_box(sd, s):
		# 		print('cannot place there', sd)
		# 		return

	if handle_mouse(e):
		return

capture = None
def handle_mouse(e):
	global capture
	if capture is not None:
		holding = capture.handle_event(e)
		if not holding:
			capture = None
		return True

	for obj in gfw.world.objects_at(gfw.layer.ui):
		if obj.handle_event(e):
			capture = obj
			return True

	return False

def pause():
	pass

def resume():
	create_state()

def exit():
	pass

def attack_mob():
	damage = 50
	if sd.attack_target() is not None:
		index = sd.attack_target()
		mob.decrease_life(damage, index)
		print("attack mob")

def set_sd():
	global sd
	sd = SD()
	gfw.world.add(gfw.layer.sd, sd)
	print("set sd")

def set_mob():
	global index
	global mob
	mob = Mob(index)
	if index < WAVE:
		gfw.world.add(gfw.layer.mob, mob)
		index += 1
		print(index, "th Mob Generated")

def set_menu():
	global button_menu
	menu_xy = gobj.set_mouse_pos(ui_x, ui_y, 1)
	button_menu = Button(*menu_xy, ui_w, ui_h, lambda:start("menu"))
	gfw.world.add(gfw.layer.ui, button_menu)

	global button_inven
	inven_xy = gobj.set_mouse_pos(ui_x, ui_y - ui_margin, 1)
	button_inven = Button(*inven_xy, ui_w, ui_h, lambda:start("inven"))
	gfw.world.add(gfw.layer.ui, button_inven)

	global button_char
	char_xy = gobj.set_mouse_pos(ui_x, ui_y - 2 * ui_margin, 1)
	button_char = Button(*char_xy, ui_w, ui_h, lambda:start("char"))
	gfw.world.add(gfw.layer.ui, button_char)

	global ui_menu
	ui_menu = gfw.image.load(gobj.RES_DIR + 'ui_menu.png')

	global ui_inven
	ui_inven = gfw.image.load(gobj.RES_DIR + 'ui_inven.png')

	global ui_char
	ui_char = gfw.image.load(gobj.RES_DIR + 'ui_char.png')

def draw_menu():
	global ui_menu, ui_inven, ui_char
	ui_menu.draw(*gobj.set_mouse_pos(ui_x, ui_y, 1))
	ui_inven.draw(*gobj.set_mouse_pos(ui_x, ui_y - ui_margin, 1))
	ui_char.draw(*gobj.set_mouse_pos(ui_x, ui_y - 2 * ui_margin, 1))

if __name__ == '__main__':
	gfw.run_main()