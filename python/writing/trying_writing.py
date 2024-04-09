print("hi")

l = ['Estaban', 'Aidan','Aidan','Matthew','Leon']


with open("written.txt", "a+") as f:
	for i in l:
		f.write(i+'\n')
	f.close()
