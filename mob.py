#start at 210112
from pico2d import *
import gobj
import gfw

class Mob:
	PAT_POSITIONS = [
		gobj.set_pos_origin(110, 70),
		gobj.set_pos_origin(670, 70),
		gobj.set_pos_origin(670, 375),
		gobj.set_pos_origin(110, 375)
	]
	images = {}
	FPS = 12
	def __init__(self):
		self.pos = gobj.set_pos_origin(110, 375)
		self.hp = 0
		self.speed = 1
		self.time = 0
		self.fidx = 0
		self.index = 0
		self.delta = (0, 0)
		self.char = 'goblin'
		Mob.load_all_images()

	def find_patrol_position(self):
		pass

	def follow_patrol_position(self):
		pass

	def set_patrol_position(self):
		x, y = self.pos
		px, py = Mob.PAT_POSITIONS[self.index]
		dx, dy = px - x, py - y
		mov_x, mov_y = 0, 0
		distance = math.sqrt(dx**2 + dy**2)
		if distance == 0: self.index += 1
		if self.index > 3:
			self.index = 0
		mov_x = self.speed if dx > 0 else -self.speed
		mov_y = self.speed if dy > 0 else -self.speed
		if dx == 0:
			mov_x = 0
		if dy == 0:
			mov_y = 0
		self.delta = mov_x, mov_y
		print(mov_x, ", ", mov_y)

	def draw(self):
		x, y = self.pos
		#pos_x, pos_y = gobj.set_image_pos(x, y)
		mob_images = self.images[self.char]
		#image = images[self.sd.fidx % len(images)]
		image = mob_images[self.fidx % len(mob_images)]
		if self.index > 1:
			flip = 'h'
			pos_x, pos_y = gobj.set_flip_pos(x, y)
		else:
			flip = ''
			pos_x, pos_y = self.pos
		image.composite_draw(0, flip, pos_x, pos_y, image.w, image.h)
		#pos_x, pos_y = self.pos
		#pos_x -= 150
		#image.draw(pos_x, pos_y, 1.5 * image.w, 1.5 * image.h)
		#images.draw(*self.pos, image.w, image.h)

	def update(self):
		self.set_patrol_position()
		self.time += gfw.delta_time
		self.fidx = round(self.time * Mob.FPS)

		x,y = self.pos
		dx, dy = self.delta
		px, py = Mob.PAT_POSITIONS[self.index]
		x += dx
		y += dy

		#check over
		done = False
		if dx > 0 and x >= px or dx < 0 and x <= px:
			x = px
			done = True
		if dy > 0 and y >= py or dy < 0 and y <= py:
			y = py
			done = True

		self.pos = x,y

		return done

	@staticmethod
	def load_all_images():
		Mob.load_images('goblin')

	@staticmethod
	def load_images(char):
		if char in Mob.images:
			return Mob.images[char]

		images = {}
		count = 0
		file_fmt = '%s/%s/%d.png'
		mob_images = []
		n = 0
		while True:
			n += 1
			fn = file_fmt % (gobj.RES_DIR, char, n)
			if os.path.isfile(fn):
				mob_images.append(gfw.image.load(fn))
			else:
				break
			count += 1
		Mob.images[char] = mob_images
		print('%d images loaded for %s' %(count, char))
		return images