def compute(srcIp, L) : # Computing 13 different metrics per node
    print("compute method called for IP: " + srcIp)
    reqRecNum = 0
    reqSentNum = 0
    reqRecByte = 0
    reqRecData = 0
    reqSentByte = 0
    reqSentData = 0

    repRecNum = 0
    repSentNum = 0
    repRecByte = 0
    repRecData = 0
    repSentByte = 0
    repSentData = 0

    for iter in range(0, len(L), 1):
	    # Data size metrics
        #print(str(L[iter][4]))
        if L[iter][4] == str(8): # tracking metrics for echo requests, index for ICMP type and comparison changed for the test packet
            if L[iter][2] == srcIp:
                reqSentNum += 1 # Number of echo requests sent
                reqSentByte = reqSentByte + (int(L[iter][3]) + 14) # echo request bytes sent- based on the total size of the frame
                reqSentData = reqSentData + (int(L[iter][3]) - 28) # echo request bytes sent sent - based on the payload size of the ICMP packet
            if L[iter][2] != srcIp:
                reqRecNum += 1 # Number of echo requests received
                reqRecByte = reqRecByte + (int(L[iter][3]) + 14) # echo request bytes received
                reqRecData = reqRecData + (int(L[iter][3]) - 28) # echo request data received

        if L[iter][4] == str(0): # tracking metrics for echo replies
            if L[iter][2] == srcIp:
                repSentNum += 1 # Number of echo replies sent
                repSentByte = repSentByte + (int(L[iter][3]) + 14) # echo reply bytes sent
                repSentData = repSentData + (int(L[iter][3]) - 28) # echo reply data
            if L[iter][2] != srcIp:
                repRecNum += 1 # Number of echo replies received
                repRecByte = repRecByte + (int(L[iter][3]) + 14) # echo reply bytes received
                repRecData = repRecData + (int(L[iter][3]) - 28) # echo reply data received
    print("ECHO REQ - Num Received: " + str(reqRecNum) + ", Num Sent: " + str(reqSentNum) + ", Bytes Received: " + str(reqRecByte))
    print("ECHO REP - Num Received: " + str(repRecNum) + ", Num Sent: " + str(repSentNum) + ", Bytes Received: " + str(repRecByte))
	# Time based metrics
		# Average Round-Trip-Time, the time between sending an Echo-Req and receiving an Echo-Rep, measured in MS
		# Echo Request Throughput (in kB/s), the sum of the frame sizes of all the Echo-Reqs sent divided by the sum of RTTs
        # Echo Request Goodput (in kB/s) the sum of the ICMP payloads of all Echo-Reqs sent divided by the sum of the RTTs
        # Avg. reply delay (in microseconds so *1000), the time between a node receiving an Echo-Req and sending an Echo-Rep

	# Distance metrics
        # Avg. number of hops per Echo-Req (one hop per change of network, min. one hop)


