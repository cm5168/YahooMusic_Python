cur_user = -1
with open("Data/test_UserList.txt",'w') as file:
	with open('RawData/testTrack_hierarchy.txt') as f:
		for line in f:
			f_list=line.strip("\n").split("|")
			if cur_user != f_list[0]:
				cur_user = f_list[0]
				file.write(cur_user+"\n")