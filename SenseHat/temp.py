print("Esteban The third Island Boy")
import matplotlib.pyplot as plt
from sense_hat import SenseHat
import time
sense = SenseHat()
y = []
x = []
i = 0
z = []

for i in range(20):
	for j in range(10):
		time.sleep(1)
		press = sense.get_temperature_from_pressure
		temp = sense.get_temperature_from_humidity
	y.append(temp)
	x.append(i)
	z.append(press)
	print(i)
	



plt.ylabel("Temperature")
plt.xlabel("Time In Seconds")
plt.title("Labratorial Temperature")
plt.legend(" Pressure Temp, Humidity temp")
plt.plot(x,y)	
plt.plot(x,z)
plt.show()
 
