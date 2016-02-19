lib_trackData = {}
with open("trackData2.txt") as trackData:
	for line in trackData:
		[track_Id,track_detail] = line.strip("\n").split("|",maxsplit = 1)
		lib_trackData[track_Id] = track_detail

with open("bTest_set1_Hierarchy.txt","w") as testHierarchy:
	with open("bTest_set1.txt") as testData:
		for line in testData:
			[cur_user,cur_track] = line.strip("\n").split("|")
			testHierarchy.write(cur_user+"|"+cur_track+"|"+lib_trackData[cur_track]+"\n")
			print(cur_user)
