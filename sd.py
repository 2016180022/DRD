#start at 210106
from pico2d import *
import gfw
import gobj

class SettingState:
	@staticmethod
	def get(sd):
		#if not hasattr(SettingState, 'singlton'):
		SettingState.singlton = SettingState()
		SettingState.singlton.sd = sd
		return SettingState.singlton

	def __init__(self):
		pass

	def enter(self):
		self.pos = (0, 0)
		self.sd.action = 'Set'
		print("now Set")
		hide_cursor()

	def exit(self):
		pass

	def draw(self):
		job_images = self.sd.images[self.sd.char]
		images = job_images['Wait']
		image = images[0]
		flip = 'h'
		image.composite_draw(0, flip, *self.pos, 1.5 * image.w, 1.5 * image.h)

	def update(self):
		pass

	def handle_event(self, e):
		if e.type == SDL_MOUSEMOTION:
			px, py = gobj.set_mouse_pos(e.x, e.y)
			x, y = gobj.set_flip_pos(px, py)
			x -= x % 60 + 50
			y -= y % 60 - 24
			self.pos = x, y
		elif e.type == SDL_MOUSEBUTTONDOWN:
			self.sd.pos = self.pos
			if self.sd.check_position():
				self.sd.set_state(WaitingState)
			else:
				print('cannot place there')
				pass

class WaitingState:
	@staticmethod
	def get(sd):
		#if not hasattr(WaitingState, 'singlton'):
		WaitingState.singlton = WaitingState()
		WaitingState.singlton.sd = sd
		return WaitingState.singlton

	def __init__(self):
		pass

	def enter(self):
		show_cursor()
		self.time = 0
		self.frame = 0
		print("now Wait")
		self.sd.action = "Wait"

	def exit(self):
		pass

	def draw(self):
		job_images = self.sd.images[self.sd.char]
		#image = images[self.sd.fidx % len(images)]
		images = job_images[self.sd.action]
		image = images[self.frame]
		flip = 'h'
		image.composite_draw(0, flip, *self.sd.pos, 1.5 * image.w, 1.5 * image.h)

	def update(self):
		frame_number = 11
		self.time += gfw.delta_time
		frame = self.time * 8
		self.frame = int(frame) % frame_number
		self.sd.set_target()

	def handle_event(self, e):
		if e.type == SDL_KEYDOWN:
			if e.key == SDLK_SPACE:
				self.sd.set_state(AttackingState)

class AttackingState:
	@staticmethod
	def get(sd):
		#if not hasattr(AttackingState, 'singlton'):
		AttackingState.singlton = AttackingState()
		AttackingState.singlton.sd = sd
		return AttackingState.singlton

	def __init__(self):
		pass

	def enter(self):
		self.time = 0
		self.frame = 0
		self.sd.action = 'Attack'
		print("now Attack")
		
	def exit(self):
		pass

	def draw(self):
		job_images = self.sd.images[self.sd.char]
		#image = images[self.sd.fidx % len(images)]
		images = job_images[self.sd.action]
		image = images[self.frame]
		pos_x, pos_y = self.sd.pos
		pos_x -= 150
		image.draw(pos_x, pos_y, 1.5 * image.w, 1.5 * image.h)
		#image.draw(50, 500, 1.5 * image.w, 1.5 * image.h)

	def update(self):
		self.time += gfw.delta_time
		frame = self.time * 8
		#frame_number = 12
		if self.frame < 12:
			self.frame = int(frame)
		else:
			self.sd.set_state(WaitingState)

	def handle_event(self, e):
		pass

class SD:
	FPS = 12
	ACTIONS = ['Set','Wait', 'Attack']
	images = {}
	def __init__(self):
		SD.load_all_images()
		self.char = 'darktemplar'
		self.action = 'Set'
		self.layer = list(gfw.world.objects_at(gfw.layer.mob))
		self.reset()

	def reset(self):
		self.pos = (200, 500)
		self.time = 0
		self.fidx = 0
		self.target_index = 0
		self.range = 250
		self.ndsq = 100000
		self.state = None
		self.set_state(SettingState)

	def set_state(self, cls):
		#if self.state != None:
			#self.state.exit()
		self.state = cls.get(self)
		self.state.enter()

	def draw(self):
		self.state.draw()

	def update(self):
		self.fidx = round(self.time * SD.FPS)
		self.state.update()

	def handle_event(self, e):
		self.state.handle_event(e)

	def remove(self):
		gfw.world.remove(self)

	def set_target(self):
		if gfw.world.count_at(gfw.layer.mob) <= 0:
			return
		x, y = self.pos
		nearest_distance = 100000
		index = 0
		nearest_index = 0
		# for i in self.layer[index]:
		# self.mob = self.layer[index]
		# mx, my = self.mob.pos
		# dsq = (x - mx)** 2 + (y - my)** 2
		# if nearest_dsq > dsq:
		# 	nearest_dsq = dsq
		# 	nearest_index = index
		# index += 1
		for i in gfw.world.objects_at(gfw.layer.mob):
			px, py = i.pos
			dx, dy = px - x, py - y
			distance = math.sqrt(dx**2 + dy**2)
			if nearest_distance > distance:
				nearest_distance = distance
				nearest_index = index
		index += 1
		self.target_index = nearest_index
		self.ndsq = nearest_distance
		print(self.ndsq)
		self.attack_target()

	def attack_target(self):
		if self.range > self.ndsq and self.action == 'Wait':
			self.set_state(AttackingState)
			return True

	def check_position(self):
		px, py = self.pos
		x, y = gobj.set_mouse_pos(px, py)
		print(x, ', ', y)
		xdone, ydone = False, False
		#if not collision()
		if x > 340 and x < 780:
			xdone = True
		if y > 120 and y < 360:
			ydone = True
		return xdone and ydone


	@staticmethod
	def load_all_images():
		SD.load_images('darktemplar')

	@staticmethod
	def load_images(char):
		if char in SD.images:
			return SD.images[char]

		images = {}
		count = 0
		file_fmt = '%s/%s/%s/%d.png'
		for action in SD.ACTIONS:
			action_images = []
			n = 0
			while True:
				n += 1
				fn = file_fmt % (gobj.RES_DIR, char, action, n)
				if os.path.isfile(fn):
					action_images.append(gfw.image.load(fn))
				else:
					break
				count += 1
			images[action] = action_images
		SD.images[char] = images
		print('%d images loaded for %s' %(count, char))
		return images
