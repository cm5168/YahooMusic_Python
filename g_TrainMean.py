##################################################################
### Summary

##################################################################
### Libraries & Functions
## Load Libraries
import time
import numpy as np


## Functions
def read_lines(file, num):
	lines = []
	line = file.readline().strip("\n").split("\t")
	lines.append(int(line[1]))
	if line:
		for i in range(1,num):
			line = file.readline().strip("\n").split("\t")
			lines.append(int(line[1]))
		return lines
	else:
		return line
		
##################################################################
### Main Program
wfile = open("Data/train_Mean.txt","w")
fUserList = open("Data/test_UserList.txt")
		
with open("RawData/trainIdx2.txt") as file:	
	uLine = fUserList.readline()
	while uLine:
		cur_user = uLine.strip("\n")
		line = file.readline()
		a = line.strip("\n").split("|")		
		lines = read_lines(file,int(a[1]))
		while int(a[0])<int(cur_user):
			line = file.readline()
			a = line.strip("\n").split("|")		
			lines = read_lines(file,int(a[1]))
		b = np.array(lines)
		wfile.write(cur_user+"|"+"%.2f"%b.mean()+"\n")			
		uLine = fUserList.readline().strip("\n")
		print(cur_user)