import random
import time
from sense_hat import SenseHat
sense = SenseHat

w = (255, 255, 255)
b = (0, 0, 0)
x = 3

commands = ['up_arrow', 'push', 'twist']

choice = random.choice(commands)


up = [
b, b, b, w, w, b, b, b,
b, b, w, w, w, w, b, b,
b, w, w, w, w, w, w, b,
b, b, w, w, w, w, b, b,
b, b, w, w, w, w, b, b,
b, b, w, w, w, w, b, b,
b, b, w, w, w, w, b, b,
b, b, w, w, w, w, b, b]

count = 0

def up_arrow():
	print("up!")
	sense.set_pixels[arrow[0]]
	s=time.time()
	up = sense.stick.wait_for_event()
	e=time.time()
	t=e-s
	if push == "up" and t<x:
		count = count + 1
	else:
		print('you lose')
		
def push():
	print('push it!')
	s=time.time()
	push = sense.stick.wait_for_event()
	e = time.time()
	t = e-s
	if push == "pressed" and t<x:
		count = count + 1
	else:
		print('you lose')
		
def twist():
	print('twist it!')
	s = gyro.get_orientation('yaw')
	wait(3)
	e = gyro=sense.get_orientation('yaw')
	if -45 < s-e < 45:
		print('you lose')


	
	
	
		

