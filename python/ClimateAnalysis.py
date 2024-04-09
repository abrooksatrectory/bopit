print("climate analysis")

import math
from pandas import *

import matplotlib.pyplot as plt

# Open the csv file
clt = read_csv('GlobalTemperatures.csv')

# Read the columns name
column_names = clt.columns.tolist()

# setting avgerage temparature to the column number 1
avg_temp = clt[column_names[1]].tolist()
# setting dt to the column number 0
dt = clt[column_names[0]].tolist()

# create an empty list
x= []
# For the years between 2015 and 1750
for i in range(2015-1750):
	# add every year number into the list
	x.append(1750+i)
# print the list x
print(x)

# setting a new list called y
y = []
# for every item in x
for j in x:
	# set l to an empty list
	l =[]
	# repeat as much time as the length of dt
	for i in range(len(dt)):
		# if the item that is going through is in the item in dt, and it is not nan
		if str(j) in str(dt[i]) and math.isnan(avg_temp[i]) == 0:
			# than add it to list l
			l.append(avg_temp[i])
	# add y the average temparature of theyear
	y.append(sum(l)/len(l))
# print the list y
print(y)
# plot x and y
plt.plot(x,y)
# show the graph
plt.show()
