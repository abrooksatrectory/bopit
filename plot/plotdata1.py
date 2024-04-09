import matplotlib.pyplot as plt

print("hi")

x = []
y = []

for i in range(100):
	x.append(i)
	y.append(i**2)

with open('data.txt','w+') as karp:
	for j in range(len(x)):
		karp.write('%4d, %4d \n' % (x[j], y[j]))

plt.plot(x,y)
plt.show()
