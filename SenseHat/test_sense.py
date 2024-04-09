print('hello')

from sense_hat import SenseHat

sense = SenseHat()

sense.set_pixel(0,0,(255,0,0))

b1 = (43,168,234)
b2 = (240,90,141)
b3 = (212, 12, 84)
b4 = (30,34,35)
b5 = (211,4,76)
b6 = (149, 87, 139)
b7 = (133,148,211)
b8 = (235, 52, 108)
b9 = (180, 116, 172)

pixels = [ 

b1, b1, b1, b1, b1, b1, b1, b1, 
b1, b1, b2, b2, b2, b2, b1, b1,
b1, b2, b2, b2, b2, b2, b2, b1, 
b1, b8, b2, b4, b2, b4, b2, b8,
b8, b2, b2, b3, b2, b3, b2, b8,
b8, b8, b5, b2, b2, b2, b5, b1,
b1, b6, b8, b8, b2, b2, b8, b1,
b1, b6, b5, b5, b1, b6, b5, b1 ]

sense.set_pixels(pixels)
