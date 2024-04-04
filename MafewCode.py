print("Spongebob")
import random
import time
from sense_hat import SenseHat
sense = SenseHat()
fail = False
num = random.randint(1,1)
win = False
if num == 1:
	e=sense.stick.get_events()
	start = time.time()
	while fail == False:
		if e[0].direction==('down') and e[0].action == "pressed":
			fail = True
			win = True
		end = time.time()
		if end - start < 0:
			fail = True
	
	
	
