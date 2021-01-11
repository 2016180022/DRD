#start at 210106
from pico2d import *
import gfw
import gobj

class WaitingState:
	@staticmethod
	def get(sd):
		if not hasattr(WaitingState, 'singlton'):
			WaitingState.singlton = WaitingState()
			WaitingState.singlton.sd = sd
		return WaitingState.singlton

	def __init__(self):
		pass

	def enter(self):
		self.time = 0
		self.frame = 0

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

	def handle_event(self, e):
		pass

class SD:
	FPS = 12
	ACTIONS = ['Wait']
	images = {}
	def __init__(self):
		SD.load_all_images()
		self.char = 'darktemplar'
		self.action = 'Wait'
		self.fidx = 0
		self.reset()

	def reset(self):
		self.pos = (200, 500)
		self.time = 0
		self.state = None
		self.set_state(WaitingState)

	def set_state(self, cls):
		if self.state != None:
			self.state.exit()
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

