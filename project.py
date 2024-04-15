import time
import random
from sense_hat import SenseHat
fail = False
sense = SenseHat()
x = random
a = (255,255,255)
b = (0,0,0)
bl = (0,0,0)
r = (255,0,0)
x = 5
y = 3

arrows= [
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

while fail == False:
	num = random.randint(0,1)
	if num == 0 and fail == False:
		start = time.time()
		sense.set_pixels(arrows[1])
		e = sense.stick.wait_for_event()
		print("left")
		end = time.time()
		#print(e)
		if end-start < limit and e.action == 'pressed' and e.direction == "left":
			#num = random.randint(0,3)
			limit = limit-0.1
			if limit <= 0:
				limit = 0.1
				score = score+1

			print("yay")

		elif e.action == 'pressed' and e.direction != "left":
	
			print("pay attention to the direction")
			sense.show_message("oops")
			fail = True

			print("YOUR SCORE IS")
	
		elif end-start > limit:
			print("Thats Time!")
			sense.show_message("Oh noooo")
			fail = True
			print("Welp... Your Score Is... ")
			
		if num == 0 and fail == False:
			start = time.time()
			sense.set_pixels(arrows[1])
			e = sense.stick.wait_for_event()
			print("right")
			end = time.time()
		#print(e)
		if end-start < limit and e.action == 'pressed' and e.direction == "right":
			#num = random.randint(0,3)
			limit = limit-0.1
		if limit <= 0:
			limit = 0.1
			score = score+1
			print("YEPEE")
		elif e.action == 'pressed' and e.direction != "right":

			print(" DIRECTION!!!")
			sense.show_message("oops")
			fail = True
			print('your score is ', score)
		elif end-start > limit:
			print(" TIME!!!")
			sense.show_message("oops")
			fail = True
			print('your score is ', score)
