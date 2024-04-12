print("Spongebob")
#import stuff
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
# set up colors
r = (255,0,0)
g = (0,255,0)
b = (0,0,0)
w = (255,255,255)
o = (255,255,0)
bl = (0,0,0)
re = (255,0,0)
# Setting arrows
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
# master loop
while fail == False:
	num = random.randint(0,1)
	# if down gets triggered
	if num == 0 and fail == False:
		# record the start time
		start = time.time()
		sense.set_pixels(arrows[1])
		# wait for the player to move the joystick
		e = sense.stick.wait_for_event()
		print("DOWN")
		#record the end time
		end = time.time()
		#print(e)
		# winning conditions, in time and is pressed and the direction is down
		if end-start < limit and e.action == 'pressed' and e.direction == "down":
			#num = random.randint(0,3)
			# reduce the time limit
			limit = limit-0.1
			# if the limit is zero then add a little on it
			if limit <= 0:
				limit = 0.1
			# add the score to the player
			score = score+1
			print("YEPEE")
		# if it is pressed, but the direction is false, then the player lose
		elif e.action == 'pressed' and e.direction != "down":
			print(" DIRECTION!!!")
			sense.show_message("oops")
			fail = True
			print('your score is ', score)
		# if the player ran out of time, the player lose
		elif end-start > limit:
			print(" TIME!!!")
			sense.show_message("oops")
			fail = True
			print('your score is ', score)
	# if the gyroscope shake it have activated
	if num == 1 and fail == False:
		# record the time
		start = time.time()
		sense.set_pixels(S)
		# while the player did not lose
		while fail == False:
			#get the value of the gryoscope
			x, y, z = sense.get_accelerometer_raw().values()
			#set every value to a positive value
			x = abs(x)
			y = abs(y)
			z = abs(z)
			# if the value is greater then three, then it means that the player is shaking the gyroscope
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
		
			

	
	
	
	
