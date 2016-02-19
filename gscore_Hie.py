##################################################################
### Libraries & Functions
## Load Libraries
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



##################################################################
### Main Program
## Define Variables
train_dict = {}
train_user = -1
start_time = time.time()

## Read file


with open('Data/test_raw_score.txt','w') as testResult:
	with open('RawData/testTrack_hierarchy.txt') as testData:
		with open('RawData/trainIdx2.txt') as trainData:
			# 6 test song for each user
			lines_test = read_lines(testData,6)
			while lines_test:
				cur_test = lines_test[0].strip("\n").split("|")
				cur_user = cur_test[0]
				#Navigate to the current user
				while int(train_user) < int(cur_user):
					lines_train = trainData.readline()
					[train_user,train_user_rates] = lines_train.strip("\n").split("|")
					lines_train = read_lines(trainData,int(train_user_rates))
					
				#Set Up Dictionary
				train_dict.clear()
				for line_train in lines_train:
					train_dict_item = line_train.strip("\n").split("\t")
					train_dict[train_dict_item[0]] = train_dict_item[1]
								
				for line_test in lines_test:
					test_song = line_test.strip("\n").split("|")
					testResult.write(cur_user+"|"+test_song[1]+"|")
					#print(cur_user,train_user,train_user_rates,time.time()-start_time)
					del test_song[:2]
					cur_rating = [train_dict[x] if x in train_dict else "None" for x in test_song ]
								
					testResult.write("|".join(cur_rating))
					testResult.write("\n")
				lines_test = read_lines(testData,6)
				print(cur_user,time.time()-start_time)
				#print("Next User")