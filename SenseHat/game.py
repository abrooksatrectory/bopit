print("HI MOM")
from sense_hat import SenseHat
sense = SenseHat()
gy = sense.get_gyroscope()

x = 4
y = 5

sense.set_pixel(x,y,(255,255,255))

while(1):
	gy = sense.get_gyroscope()

