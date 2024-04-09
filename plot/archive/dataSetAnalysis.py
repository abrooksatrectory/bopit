print("hi")

from pandas import *

net = read_csv("Spotify_Youtube.csv")

column_names = net.columns.tolist()
print(column_names)

tracks = net[column_names[3]].tolist()
singer = net[column_names[1]].tolist()

songs = []

for i in range(len(tracks)):
	if 'Taylor Swift' in str(singer[i]):
		songs.append(tracks[i])
		print(tracks[i])

#print(songs)

#for j in songs:
#	print(j)
#des = net["description"].tolist()

#print(des[5])
