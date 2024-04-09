
print("estarizz")
import time
from sense_hat import SenseHat
import random as rn
x = rn
sense = SenseHat()
b = (255,255,255)
a = (0,0,0)
arrows = [[
a,a,a,b,b,a,a,a,
a,b,b,b,b,b,a,a,
a,b,b,b,b,b,b,a,
a,b,b,b,b,b,b,a,
a,a,b,b,b,b,a,a,
a,a,b,b,b,b,a,a,
a,a,b,b,b,b,a,a,
a,a,b,b,b,b,a,a
],[
a,a,b,b,b,b,a,a,
a,a,b,b,b,b,a,a,
a,a,b,b,b,b,a,a,
a,a,b,b,b,b,a,a,
a,b,b,b,b,b,b,a,
a,a,b,b,b,b,a,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a
],[
a,a,a,a,a,b,a,a,
b,b,b,b,b,b,b,a,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
a,a,a,a,b,b,b,a,
a,a,a,a,a,b,a,a
],[
a,a,a,b,a,a,a,a,
a,a,b,b,a,a,a,a,
a,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
a,b,b,b,b,b,b,b,
a,a,b,b,a,a,a,a,
a,a,a,b,a,a,a,a
]]

while(1):
	start = time.time()
	end = time.time()
	speed = abs(start-end)
	e=sense.stick.wait_for_event()
	print(e.direction)
	
	count = ['up', 'down', 'right', 'left']
	x = rn.randint(0,4)
	sense.set_pixels(arrows[x])
	game = 1

limit = 5
fail = False
s = time.time()
event = sense.stick.wait_for_event()
e=time.time()
t = (e-s)
if t<5 and event.action == "pressed" and even.direction == l[x]:
	x=randint(0,4)
	sense.set_pixels(arrows[x])
elif event.action == "pressed" and t>5 or event.direction != l[x]:
	fail = False




