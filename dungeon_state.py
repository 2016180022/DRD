#start at 210127
from pico2d import *
import gobj
import gfw
from button import Button
import game_state

canvas_width = game_state.canvas_width
canvas_height = game_state.canvas_height
x, y, w, h = 440, 160, 500, 80
margin = 90

def start(stage):
	game_state.stage = stage
	gfw.push(game_state)

def enter():
	create_state()

def create_state():
	gfw.world.init(['bg', 'button'])

	bg = gobj.ImageObject('dungeon_bg.png', canvas_width//2, canvas_height//2, canvas_width, canvas_height)
	gfw.world.add(gfw.layer.bg, bg)

	set_button()

def update():
	gfw.world.update()

def draw():
	gfw.world.draw()

	draw_button()

	gobj.draw_collision_box()

def handle_event(e):
	if e.type == SDL_QUIT:
		return gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			return gfw.pop()

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

def set_button():
	global forest_button
	forest_xy = gobj.set_mouse_pos(x, y, 1)
	forest_button = Button(*forest_xy, w, h, lambda: start("demo"))
	gfw.world.add(gfw.layer.button, forest_button)

	global heaven_button
	heaven_xy = gobj.set_mouse_pos(x, y + margin, 1)
	heaven_button = Button(*heaven_xy, w, h, lambda: start("demo"))
	gfw.world.add(gfw.layer.button, heaven_button)

	global evildom_button
	evildom_xy = gobj.set_mouse_pos(x, y + 2 * margin, 1)
	evildom_button = Button(*evildom_xy, w, h, lambda: start("demo"))
	gfw.world.add(gfw.layer.button, evildom_button)

	global wisdom_button
	wisdom_xy = gobj.set_mouse_pos(x, y + 3 * margin, 1)
	wisdom_button = Button(*wisdom_xy, w, h, lambda: start("wisdom"))
	gfw.world.add(gfw.layer.button, wisdom_button)

	global img_forest_button_blue, img_forest_button_gold
	img_forest_button_blue = gfw.image.load(gobj.RES_DIR + 'forest_button_blue.png')
	img_forest_button_gold = gfw.image.load(gobj.RES_DIR + 'forest_button_gold.png')

	global img_heaven_button_blue, img_heaven_button_gold
	img_heaven_button_blue = gfw.image.load(gobj.RES_DIR + 'heaven_button_blue.png')
	img_heaven_button_gold = gfw.image.load(gobj.RES_DIR + 'heaven_button_gold.png')

	global img_evildom_button_blue, img_evildom_button_gold
	img_evildom_button_blue = gfw.image.load(gobj.RES_DIR + 'evildom_button_blue.png')
	img_evildom_button_gold = gfw.image.load(gobj.RES_DIR + 'evildom_button_gold.png')

	global img_wisdom_button_blue, img_wisdom_button_gold
	img_wisdom_button_blue = gfw.image.load(gobj.RES_DIR + 'wisdom_button_blue.png')
	img_wisdom_button_gold = gfw.image.load(gobj.RES_DIR + 'wisdom_button_gold.png')

def draw_button():
	global forest_button
	global img_forest_button_blue, img_forest_button_gold
	if forest_button.capture == True:
		img_forest_button_gold.draw(*gobj.set_mouse_pos(x, y, 1))
	else:
		img_forest_button_blue.draw(*gobj.set_mouse_pos(x, y, 1))

	global heaven_button
	global img_heaven_button_blue, img_heaven_button_gold
	if heaven_button.capture == True:
		img_heaven_button_gold.draw(*gobj.set_mouse_pos(x, y + margin, 1))
	else:
		img_heaven_button_blue.draw(*gobj.set_mouse_pos(x, y + margin, 1))

	global evildom_button
	global img_evildom_button_blue, img_evildom_button_gold
	if evildom_button.capture == True:
		img_evildom_button_gold.draw(*gobj.set_mouse_pos(x, y + 2 * margin, 1))
	else:
		img_evildom_button_blue.draw(*gobj.set_mouse_pos(x, y + 2 * margin, 1))

	global wisdom_button
	global img_wisdom_button_blue, img_wisdom_button_gold
	if wisdom_button.capture == True:
		img_wisdom_button_gold.draw(*gobj.set_mouse_pos(x, y + 3 * margin, 1))
	else:
		img_wisdom_button_blue.draw(*gobj.set_mouse_pos(x, y + 3 * margin, 1))

def is_captured(obj):
	if obj.capture == True:
		return True

def exit():
	print("dungeon_state exits")

def pause():
	pass

def resume():
	create_state()

if __name__ == '__main__':
	gfw.run_main()