import random as rn
import time
from sense_hat import SenseHat

sense = SenseHat()

w = (255, 255, 255)
b = (0, 0, 0)
x = 3

count = 0
life = 1

def up_arrow(x, count, life):
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
	sense.clear
	if push == "up" and t<x:
		count = count + 1
		x = x - 0.1
	else:
		life = life - 1
		print('you lose')
		
def push(x, count, life):
	print('push it!')
	s=time.time()
	push = sense.stick.wait_for_event()
	e = time.time()
	t = e-s
	if push == "pressed" and t<x:
		count = count + 1
		x = x - 0.1
	else:
		life = life - 1
		print('you lose')
		
def twist(x, count, life):
	s = 0
	e = 0
	print("twist it!")
	while -45 < s-e < 45:
		st = time.time()
		sw = sense.get_orientation_degrees()
		s = sw['yaw']
		time.sleep(3)
		ew = sense.get_orientation_degrees()
		e = ew['yaw']
		et = time.time()
		t = et-st
		if t >= 3:
			life = life - 1
			print('you lose')
		elif e-s > 45 or e-s < - 45:
			count = count + 1
			x = x - 1



while(1):
	if life == 0:
		break
	num = rn.randint(1,3)
	if num == 1:
		up_arrow(x, count, life)
	elif num == 2:
		push(x, count, life)
	elif num == 3:
		twist(x, count, life)

print("game over. Final score: " + str(count))
		

