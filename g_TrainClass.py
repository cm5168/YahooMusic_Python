##################################################################
### Libraries & Functions
## Load Libraries
import time

## Functions

##################################################################
### Main Program
## Define Variables

## Load Album, Artist, Genre Data
class_lib = {}
# Load Album
with open('RawData/albumData2.txt') as f:
	for line in f:
		temp = line.strip("\n").split("|")
		class_lib[temp[0]] = 2
# Load Artist
with open('RawData/artistData2.txt') as f:
	for line in f:
		class_lib[line.strip("\n")] = 3
# Load Genre
with open('RawData/genreData2.txt') as f:
	for line in f:
		class_lib[line.strip("\n")] = 4

## Read file
start_time = time.time()

with open('Data/train_ClassifiedCount.txt','w') as trainMod:
		with open('RawData/trainIdx2.txt') as trainData:
			for line in trainData:
				if '|' in line:
					[cur_user,cur_user_rates] = line.strip("\n").split("|")
					print('Current User is',end =' ')
					print(cur_user,end=' ')
					print("spend %.2f s"%(time.time()-start_time))
					trainMod.write(cur_user+"|"+cur_user_rates+"\n")
				else:
					[cur_item,cur_item_rate] = line.strip("\n").split("\t")
					if cur_item in class_lib:
						cur_item_class = class_lib[cur_item]
					else:
						cur_item_class = 1
					trainMod.write(cur_item+"|"+cur_item_rate+"|"+str(cur_item_class)+"\n")