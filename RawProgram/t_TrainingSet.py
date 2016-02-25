##Extract list of all users from testTrack_hierarchy
from operator import itemgetter
import time

## Functions
def read_lines(file, num):
	lines = []
	line = file.readline()
	lines.append(line)
	if line:
		for i in range(1,num):
			lines.append(file.readline())
		return lines
	else:
		return line
## Variables

## Load Files
fUserList = open("Data/test_UserList.txt")
fNewTest = open("TrainingData/eTestSet_Hierarchy.txt","w")
fNewTest_Result = open("TrainingData/eTestSet_TrueResult.txt","w")
fUserMean = open("Data/train_Mean.txt")

lib_trackData = {}
with open("RawData/trackData2.txt") as trackData:
	for line in trackData:
		[track_Id,track_detail] = line.strip("\n").split("|",maxsplit = 1)
		lib_trackData[track_Id] = track_detail
		
start_time = time.time()

train_TrackList = []
train_TrackList_temp = []

## Main Program

with open("Data/train_Classified.txt") as trainData:
	cur_user = fUserList.readline().strip("\n")
	trainLine = trainData.readline().strip("\n").split("|")
	while cur_user:
		userMean = fUserMean.readline().strip("\n").split("|")
		# Check Error if User and UserMean are not match
		if userMean[0] != cur_user:
			print("User and User's Mean are not match")
			break		
			
		userMean = float(userMean[1])
		if userMean > 40:
			userMean = 40
		
		while int(trainLine[0]) < int(cur_user):
			trainLine = trainData.readline().strip("\n").split("|")
		del train_TrackList[:]
		del train_TrackList_temp[:]
		while int(trainLine[0]) == int(cur_user):
			if trainLine[3] == "1":
				train_TrackList.append([trainLine[1],int(trainLine[2])])
			trainLine = trainData.readline().strip("\n").split("|")
		
		if len(train_TrackList) <= 12:
			fNewTest.write(cur_user+"|"+str(len(train_TrackList))+"|"+str(userMean)+"\n")
			fNewTest_Result.write(cur_user+"|"+str(len(train_TrackList))+"|"+str(userMean)+"\n")
			for item in train_TrackList:
				fNewTest.write(item[0]+"|"+lib_trackData[item[0]]+"\n")
				fNewTest_Result.write(item[0]+"|"+str(item[1])+"|"
					+("0" if item[1]<userMean else "1")+"\n")
		else:
			train_TrackList = sorted(train_TrackList, key = itemgetter(1))
			train_TrackListH = [x for x in train_TrackList if x[1] >= userMean]
			train_TrackListL = [x for x in train_TrackList if x[1] < userMean]
			if len(train_TrackListH) <= 6:
				lenH = len(train_TrackListH)
				if lenH == 0:
					pass
				elif lenH == 1:
					train_TrackList_temp.extend(train_TrackListH)
				else:
					train_TrackList_temp.extend(train_TrackListH)
			else:
				train_TrackList_temp.extend(train_TrackListH[:4])
				train_TrackList_temp.extend(train_TrackListH[-2:])
				lenH = 6
			if len(train_TrackListL) <= 6:
				lenL = len(train_TrackListL)
				if lenL == 0:
					pass
				elif lenL == 1:
					train_TrackList_temp.extend(train_TrackListL)
				else:
					train_TrackList_temp.extend(train_TrackListL)
			else:
				train_TrackList_temp.extend(train_TrackListL[:2])
				train_TrackList_temp.extend(train_TrackListL[-4:])
				lenL = 6
				
			fNewTest.write(cur_user+"|"+str(lenH+lenL)+"|"+str(userMean)+"\n")
			fNewTest_Result.write(cur_user+"|"+str(lenH+lenL)+"|"+str(userMean)+"\n")
			try:
				for item in train_TrackList_temp:
					fNewTest.write(item[0]+"|"+lib_trackData[item[0]]+"\n")
					fNewTest_Result.write(item[0]+"|"+str(item[1])+"|"
						+("0" if item[1]<userMean else "1")+"\n")
			except:
				print(item,train_TrackList_temp)
				break
		
		print(cur_user,"Spend %.2f s"%(time.time()-start_time), )	
		cur_user = fUserList.readline().strip("\n")
		
'''		
for test_linea in test_TrackList:
	fNewTest.write(str(test_linea[0])+"|"+str(test_linea[1])+"\n")
	fNewTest_Result.write(str(test_linea[0])+"|"+str(test_linea[1])+"|"+str(test_linea[2])+"\n")
'''

fUserList.close()
fNewTest.close()
fNewTest_Result.close()
fUserMean.close()