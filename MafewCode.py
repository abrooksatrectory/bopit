print("Spongebob")
import random
import time
from sense_hat import SenseHat
sense = SenseHat()
fail = False
num = random.randint(1,1)
win = False
limit = 10
score = 0
e=sense.stick.get_events()
r = (255,0,0)
g = (0,255,0)
b = (0,0,0)
w = (255,255,255)
o = (255,255,0)
bl = (0,0,0)
re = (255,0,0)
arrows= [[
bl,bl,bl,r,r,bl,bl,bl,
bl,bl,r,r,r,r,bl,bl,
bl,r,r,r,r,r,r,bl,
r,r,r,r,r,r,r,r,
bl,bl,r,r,r,r,bl,bl,
bl,bl,r,r,r,r,bl,bl,
bl,bl,r,r,r,r,bl,bl,
bl,bl,r,r,r,r,bl,bl],
[
bl,bl,r,r,r,r,bl,bl,
bl,bl,r,r,r,r,bl,bl,
bl,bl,r,r,r,r,bl,bl,
bl,bl,r,r,r,r,bl,bl,
r,r,r,r,r,r,r,r,
bl,r,r,r,r,r,r,bl,
bl,bl,r,r,r,r,bl,bl,
bl,bl,bl,r,r,bl,bl,bl,],
[
bl,bl,bl,bl,r,bl,bl,bl,
bl,bl,bl,bl,r,r,bl,bl,
r,r,r,r,r,r,r,bl,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,bl,
bl,bl,bl,bl,r,r,bl,bl,
bl,bl,bl,bl,r,bl,bl,bl,],
[
bl,bl,bl,r,bl,bl,bl,bl,
bl,bl,r,r,bl,bl,bl,bl,
bl,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
bl,r,r,r,r,r,r,r,
bl,bl,r,r,bl,bl,bl,bl,
bl,bl,bl,r,bl,bl,bl,bl,]]

S = [
b,b,b,b,b,b,b,b,
b,b,r,r,r,r,b,b,
b,b,r,b,b,b,b,b,
b,b,r,b,b,b,b,b,
b,b,r,r,r,r,b,b,
b,b,b,b,b,r,b,b,
b,b,b,b,b,r,b,b,
b,b,r,r,r,r,b,b,]
while fail == False:
	num = random.randint(0,1)
	if num == 0 and fail == False:
		start = time.time()
		sense.set_pixels(arrows[1])
		e = sense.stick.wait_for_event()
		print("DOWN")
		end = time.time()
		#print(e)
		if end-start < limit and e.action == 'pressed' and e.direction == "down":
			#num = random.randint(0,3)
			limit = limit-0.1
			if limit <= 0:
				limit = 0.1
			score = score+1
			print("YEPEE")
		elif e.action == 'pressed' and e.direction != "down":
			print(" DIRECTION!!!")
			sense.show_message("oops")
			fail = True
			print('your score is ', score)
		elif end-start > limit:
			print(" TIME!!!")
			sense.show_message("oops")
			fail = True
			print('your score is ', score)

	if num == 1 and fail == False:
		start = time.time()
		sense.set_pixels(S)
		while fail == False:
			x, y, z = sense.get_accelerometer_raw().values()

			x = abs(x)
			y = abs(y)
			z = abs(z)

			if x > 3 or y > 3 or z > 3 :
				end = time.time()
				if end-start < limit:
					limit = limit-0.1
					if limit <= 0:
						limit = 0.05
					score = score+1
					print("YEPEE")
					break
				else:
					print("TIME!!!!!")
					fail = True
		
			

	
	
	
	
