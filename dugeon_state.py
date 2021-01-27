#start at 210127
from pico2d import *
import gobj
import gfw
from button import Button

canvas_width = 720
canvas_height = 480

def start(stage):
	print(stage)

def enter():
	gfw.world.init(['bg', 'button'])

	bg = gobj.ImageObject('dungeon_bg.png', canvas_width//2, canvas_height//2, canvas_width, canvas_height)
	gfw.world.add(gfw.layer.bg, bg)

	x, y, w, h = 440, 160, 500, 80
	forest_button = Button(x, y, w, h, lambda: start("enemy"))
	gfw.world.add(gfw.layer.button, forest_button)

	global img_forest_button_blue
	img_forest_button_blue = gfw.image.load(gobj.RES_DIR + 'forest_button_blue.png')
	img_forest_button_gold = gfw.image.load(gobj.RES_DIR + 'forest_button_gold.png')


def exit():
	pass

def update():
	gfw.world.update()

def draw():
	gfw.world.draw()
	global img_forest_button_blue
	img_forest_button_blue.draw(*gobj.set_mouse_pos(440, 160, 1))
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

if __name__ == '__main__':
	gfw.run_main()