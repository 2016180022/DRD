#start at 210121
from pico2d import *
import gfw
import gobj
from mob import Mob

WAVE = 10

def init():
	global time
	global count
	time = 0
	count = 0
	#print('mg init')

def generate_mob():
	global time
	global count
	time += gfw.delta_time
	if count < WAVE:
		if time >= 1:
			mob = Mob()
			gfw.world.add(gfw.layer.mob, mob)
			time = 0
			count += 1
			#print(time)
	else:
		return False
