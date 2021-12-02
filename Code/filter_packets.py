
#Project 2
#filtering wiresharks for ICMP packets


def filter( filename) :
	f = open( filename + ".txt", 'r' )
	line = f.readline()
	L = list()

	while "\n" in line:
		if "ICMP" in line:
			if ("Echo (ping) reply") in line :
				splitline = line.strip().split()
				L.append(splitline)
				
			elif ("Echo (ping) request") in line :
				splitline = line.strip().split()	
				L.append(splitline)
				
		
		line = f.readline()

	writefile = open( filename + "_filter.csv", 'w' )
	for iter in L:
   		writefile.write(iter[0] + "," + iter[1] + "," + iter[2] + "," + iter[3] + "," + iter[4] + "," + iter[5]  + "," + iter[6] + " " + iter[7] + " " + iter[8] + "," + iter[9] + iter[10] + iter[11] + "," + iter[12] + " " + iter[13] + " " + iter[14] + "\n")
    
	f.close()
	writefile.close()	
	




