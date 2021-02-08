#start at 210205
from pico2d import *
import gfw
import gobj
from button import Button
from invensd import Invensd

#in h_e, collision check and return x, y pos to button output
#add moveable button into button.py and output button image in moveable button
canvas_width = 720
canvas_height = 480

x, y = 110, 105
x_margin = 90
y_margin = 100

ui_margin = 20
ui_w = 100
ui_h = 21

ui_x_move = 50
ui_y_move = -20

LBTN_DOWN = (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)

def next(text):
	print(text)
	if text == 'set':
		set_mode(True)
		return gfw.pop()
		#pop and call set_sd function

def enter():
	gfw.world.init(['bg', 'sd', 'ui', 'button'])

	bg = gobj.ImageObject('inven_char.png', canvas_width // 2, canvas_height // 2, canvas_width, canvas_height)
	gfw.world.add(gfw.layer.bg, bg)

	sd = Invensd(*gobj.set_mouse_pos(x, y, 1), 'darktemplar')
	sd2 = Invensd(*gobj.set_mouse_pos(x + x_margin, y, 1), 'demonslayer')
	gfw.world.add(gfw.layer.sd, sd)
	gfw.world.add(gfw.layer.sd, sd2)

	global image_ui_set, image_ui_equip
	image_ui_set = gfw.image.load(gobj.RES_DIR + 'ui_set.png')
	image_ui_equip = gfw.image.load(gobj.RES_DIR  + 'ui_equip.png')

	global captured
	captured = False

def exit():
	pass

def handle_event(e):
	if e.type == SDL_QUIT:
		return gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			return gfw.pop()

	x, y, = e.x, e.y
	pair = (e.type, e.button)
	global captured, captured_pos
	if pair == LBTN_DOWN:
		for sd in gfw.world.objects_at(gfw.layer.sd):
			if gobj.pt_in_rect(gobj.set_mouse_pos(e.x, e.y, 1), sd.get_bb()):
				captured = True
				captured_pos = sd.x, sd.y
				set_button(sd.x, sd.y)
			else:
				captured = False
				del_button()

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

	for obj in gfw.world.objects_at(gfw.layer.button):
		if obj.handle_event(e):
			capture = obj
			return True

	return False

def update():
	gfw.world.update()
	# for sd in gfw.world.objects_at(gfw.layer.sd):
	# 	print(sd.x, ', ', sd.y)

def draw():
	gfw.world.draw()
	gobj.draw_collision_box()
	global captured_pos
	if captured:
		x, y = captured_pos
		x += ui_x_move
		y += ui_y_move
		image_ui_set.draw(x, y)
		image_ui_equip.draw(x, y - ui_margin)


def set_button(x, y):
	x += ui_x_move
	y += ui_y_move
	global button_ui_set, button_ui_equip
	button_ui_set = Button(x, y, ui_w, ui_h, lambda:next("set"))
	button_ui_equip = Button(x, y - ui_margin, ui_w, ui_h, lambda:next("equip"))

	gfw.world.add(gfw.layer.button, button_ui_set)
	gfw.world.add(gfw.layer.button, button_ui_equip)

def del_button():
	gfw.world.clear_at(gfw.layer.button)
	# global button_ui_set, button_ui_equip
	# gfw.world.remove(button_ui_set)
	# gfw.world.remove(button_ui_equip)

def set_mode(set_type = False):
	return set_type

if __name__ == '__main__':
	gfw.run_main()