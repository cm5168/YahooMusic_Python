##################################################################
### Summary
# Generate the list of tracks under same album for each track in testing.


##################################################################
### Libraries & Predefined Functions
## Load Libraries
from __future__ import print_function
from operator import itemgetter
import time

## Functions


##################################################################
### Main Program
## Variables
start_time = time.time()
lists=[]

## Generate tracks corresponding to album
with open('RawData/trackData2.txt') as albumData:
	for line in albumData:
		album = line.strip("\n").split("|")
		if album[1]!="None":
			lists.append([album[1],album[0]])
		print(album[0])#," %.2f s"%(time.time()-start_time))

## Generate format Album|Track1|Track2|...|TrackN
lists = sorted(lists, key=itemgetter(0))
cur_album = -1
x=0

with open('Data/lib_album_track.txt','w') as file:
	for item in lists:
		if item[0]!= cur_album:
			cur_album = item[0]
			file.write('\n'*x+str(item[0])+"|"+str(item[1]))
			x=1
		else:
			file.write("|"+str(item[1]))
			
## Build Album-Track library
trainAlbumDict={}
with open("Data/lib_album_track.txt") as trainAlbum:
	for line_album in trainAlbum:
		test_album = line_album.strip("\n").split("|",maxsplit=1)
		trainAlbumDict[test_album[0]]=test_album[1]
	
	
## Generate Track items under same album for test dataset
with open('Data/test_album_track.txt','w') as testAlbum:
	with open('RawData/testTrack_hierarchy.txt') as testTrack:
		for line_test in testTrack:
			test_track = line_test.strip("\n").split("|")
			line_txt = test_track[0]+'|'+test_track[1]+'|'+test_track[2]
			print(test_track[0])#," %.2f s"%(time.time()-start_time))
			if test_track[2]!="None":
				test_AlbumTrk=trainAlbumDict[test_track[2]]
				testAlbum.write(line_txt+"|"+test_AlbumTrk+"\n")
			else:
				testAlbum.write(line_txt+"\n")
				
print("Finished, Spend %.2f s"%(time.time()-start_time))
