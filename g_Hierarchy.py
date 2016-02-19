lib_trackData = {}
with open("RawData/trackData2.txt") as trackData:
	for line in trackData:
		[track_Id,track_detail] = line.strip("\n").split("|",maxsplit = 1)
		lib_trackData[track_Id] = track_detail

with open("RawData/testTrack_hierarchy.txt","w") as testHierarchy:
	with open("RawData/testIdx2.txt") as testData:
		for line in testData:
			if "|" in line:
				[cur_user,cur_track] = line.strip("\n").split("|")
			else:
				cur_track = line.strip("\n")
				testHierarchy.write(cur_user+"|"+cur_track+"|"+lib_trackData[cur_track]+"\n")
			print(cur_user)
