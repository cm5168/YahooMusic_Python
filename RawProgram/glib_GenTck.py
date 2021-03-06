##################################################################
### Summary


##################################################################
### Libraries & Predefined Functions
## Load Libraries
from operator import itemgetter
import time

## Functions


##################################################################
### Main Program
## Variables
start_time = time.time()
lists=[]
genreData = []
## Generate tracks corresponding to album
with open('RawData/trackData2.txt') as trackData:
	for line in trackData:
		track_info = line.strip("\n").split("|")
		if len(track_info) > 3:
			del track_info[1]
			del track_info[1]
			genreData.append(track_info)
			
## Generate tracks corresponding to album
for album in genreData:
	for i in range(1,len(album)):
		if album[i]!="None":
			lists.append([int(album[i]),album[0]])
	print(album[0])#," %.2f s"%(time.time()-start_time))


		
## Generate format Album|Track1|Track2|...|TrackN
lists = sorted(lists, key=itemgetter(0))
cur_artist = -1
x=0

with open('Data/lib_genre_track.txt','w') as file:
	for item in lists:
		if item[0]!= cur_artist:
			cur_artist = item[0]
			file.write('\n'*x+str(item[0])+"|"+str(item[1]))
			x=1
		else:
			file.write("|"+str(item[1]))

print("Spend %.2f s"%(time.time()-start_time))