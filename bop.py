import random as rn
import time
from sense_hat import SenseHat

sense = SenseHat()

w = (255, 255, 255)
b = (0, 0, 0)
x = 3

count = 0
life = 1

def up_arrow(x, count):
	print("up!")
	up = [
b, b, b, w, w, b, b, b,
b, b, w, w, w, w, b, b,
b, w, w, w, w, w, w, b,
b, b, w, w, w, w, b, b,
b, b, w, w, w, w, b, b,
b, b, w, w, w, w, b, b,
b, b, w, w, w, w, b, b,
b, b, w, w, w, w, b, b]
	
	sense.set_pixels(up)
	s=time.time()
	up_var = sense.stick.wait_for_event()
	e=time.time()
	t=e-s
	if push == "up" and t<x:
		count = count + 1
		x = x - 0.1
	else:
		life = 0
		print('you lose')
		
def push(x, count):
	print('push it!')
	s=time.time()
	push = sense.stick.wait_for_event()
	e = time.time()
	t = e-s
	if push == "pressed" and t<x:
		count = count + 1
		x = x - 0.1
	else:
		life = 0
		print('you lose')
		
def twist(x, count):
	print('twist it!')
	sw = sense.get_orientation_degrees()
	s = sw['yaw']
	time.sleep(3)
	ew = sense.get_orientation_degrees()
	e = ew['yaw']
	if -45 < s-e < 45:
		life = 0
		print('you lose')
	else:
		count = count + 1
		x = x - 0.1




while(life == 1):
	num = rn.randint(1,3)
	if num == 1:
		up_arrow(x, count)
	elif num == 2:
		push(x, count)
	elif num == 3:
		twist(x, count)
print("game over. Final score: " + str(count))
		

