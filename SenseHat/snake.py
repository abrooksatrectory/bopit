print("Estaban the Rizzler") 
from sense_hat import SenseHat
import random as rn
import time
sense = SenseHat()
a = 0
b = 0
x = 5
y = 3
mova = 0
movb = 0
sense.clear()
x = rn.randint(0,7)
y = rn.randint(0,7)
ge = 1
xpos = [0]
ypos = [0]
i = -1
p = 0

while ge == 1:
	event=sense.stick.get_events()
	sense.set_pixel(x,y,(255,0,0))
	sense.set_pixel(a,b,(255,255,255))
	
	
	time.sleep(0.5)	
	
	if len(event)>0:
		if event[0].action == "pressed" and event[0].direction == "up":	
			mova = 0
			movb = -1
		elif event[0].action == "pressed" and event[0].direction == "down":
			mova = 0
			movb = 1
		elif event[0].action == "pressed" and event[0].direction == "left":
			mova = -1
			movb = 0
		elif event[0].action == "pressed" and event[0].direction == "right":	
			mova = 1
			movb = 0
	a = a + mova
	b = b + movb
	
	
	xpos.append(a)
	ypos.append(b)
	sense.set_pixel(xpos[i-p], ypos[i-p], (0,0,0))
	
	if x == a and y == b:
		x = rn.randint(0,7)
		y = rn.randint(0,7)
		p = p + 1
	if a > 7:
		sense.clear()
		ge = 0
		
	if b > 7:
		sense.clear()
		ge = 0
	i = i + 1	
	
	
	

		
		
	
	
