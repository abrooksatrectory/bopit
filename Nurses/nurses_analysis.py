from pandas import *

clt = read_csv("people-1000.csv")

column_names = clt.columns.tolist()

sex = clt[column_names[4]].tolist()
date = clt[column_names[7]].tolist()
job = clt[column_names[8]].tolist()


count = 0

years = []
for i in date:
	p = i.split("-")
	years.append(p[0])
	
for i in range(len(sex)):
	if 'Male' in sex[i] and 'Nurse' in job[i] and int(years[i])>=1980:
		count = count + 1 

print(count)
