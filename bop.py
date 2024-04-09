import random
import time
from sense_hat import SenseHat
sense = SenseHat
w = (255, 255, 255)
b = (0, 0, 0)
arrow = ['up']
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
	push = sense.stick.wait_for_event()
	e=time.time()
	t=e-s
	if push == "up" and t<3:
		count = count + 1
		

