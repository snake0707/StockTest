import config

def processMA(data, t = 5):
	curdata = map(list, data)
	MAculist = []
	i_end = config.getEndNum()

	#i = 0
	for row in curdata:
		# 0:date 	1:time
		#print(row)
		#print(MAculist)
		#print(len(MAculist))
		#print(t)
		MAculist.append(row[i_end])
		if len(MAculist) > t:
			del MAculist[0]
		
		avg = average(MAculist)
		row.append(avg)

	return curdata

def average(list):
	sum = 0
	for num in list:
		sum += num
	avg = sum / len(list)
	return avg

def processKDJ(data):
	curdata = map(list, data)
	KDJHighlist = []
	KDJLowlist = []
	Klist = []
	Dlist = []
	i_end = config.getEndNum()
	i_high = config.getHighNum()
	i_low = config.getLowNum()
	day = config.getKDJDay()

	for row in curdata:
		KDJHighlist.append(row[i_high])
		KDJLowlist.append(row[i_low])
		if len(KDJHighlist) > day:
			del KDJHighlist[0]
		if len(KDJLowlist) > day:
			del KDJLowlist[0]

		high_n = high(KDJHighlist)
		low_n = low(KDJLowlist)
		c_n = row[i_end]

		Klast = 50
		Dlast = 50

		if len(Klist) > 0:
			Klast = Klist[-1]
			#print(Klast)
		if len(Dlist) > 0:
			Dlast = Dlist[-1]

		if high_n == low_n:
			RSV_n = 0
		else:
			RSV_n = (c_n - low_n) / (high_n - low_n) * 100

		K = 2.0 / 3.0 * Klast + 1.0 / 3.0 * RSV_n
		D = 2.0 / 3.0 * Dlast + 1.0 / 3.0 * K
		J = 3 * K - 2 * D
		
		Klist.append(K)
		Dlist.append(D)

		row.append(K)
		row.append(D)
		row.append(J)
	return curdata

def high(list):
	high = list[0]
	for num in list:
		if num > high:
			high = num
	return high

def low(list):
	low = list[0]
	for num in list:
		if num < low:
			low = num
	return low
