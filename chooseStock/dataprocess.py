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

def processDonchian(data, tHigh = 20, tLow = 10):
	curdata = map(list, data)

	donchianHighList = []
	donchianLowList = []

	i_end = config.getEndNum()
	i_high = config.getHighNum()
	i_low = config.getLowNum()

	for row in curdata:
		if len(donchianHighList) == 0:
			high_n = 0
		else :
			high_n = high(donchianHighList)
		if len(donchianLowList) == 0:
			low_n = 0
		else :
			low_n = low(donchianLowList)

		row.append(high_n)
		row.append(low_n)

		donchianHighList.append(row[i_high])
		donchianLowList.append(row[i_low])
		if len(donchianHighList) > tHigh:
			del donchianHighList[0]
		if len(donchianLowList) > tLow:
			del donchianLowList[0]

	return curdata

def processSnakeStrategy_1(data, dayLast = 3):
	curdata = map(list, data)
	#print(curdata)

	addData = [0, 0, 0, 0, 0, 0, 0]
	curdata.append(addData)
	#print(curdata)

	sSEndList = []
	sSHighList = []
	sSLowList = []

	i_end = config.getEndNum()
	i_high = config.getHighNum()
	i_low = config.getLowNum()

	for row in curdata:
		if len(sSEndList) == 0:
			ma_n = row[i_end]
			high_n = row[i_high]
			low_n = row[i_low]

			end_last = row[i_end]
		else :
			ma_n = average(sSEndList)
			high_n = high(sSHighList)
			low_n = low(sSLowList)

			end_last = sSEndList[-1]

		# change N aver price to last day end price
		# end_last = row[i_end]
		# end_last = sSEndList[-1]

		buyPrice = (end_last + low_n) / 2
		sellPrice = (end_last + high_n) / 2

		# buyPrice = (ma_n + low_n) / 2
		# sellPrice = (ma_n + high_n) / 2
		row.append(buyPrice)
		row.append(sellPrice)

		sSEndList.append(row[i_end])
		sSHighList.append(row[i_high])
		sSLowList.append(row[i_low])
		if len(sSEndList) > dayLast:
			del sSEndList[0]
			del sSHighList[0]
			del sSLowList[0]

	return curdata


def processDualThrust(data, tN = 10, Ks = 0.5, Kx = 0.5):
	curdata = map(list, data)

	nDayHighList = []
	nDayEndList = []
	nDayLowList = []

	i_open = config.getOpenNum()
	i_end = config.getEndNum()
	i_high = config.getHighNum()
	i_low = config.getLowNum()

	for row in curdata:
		if len(nDayEndList) == 0:
			hHn = 0.0
			hEn = 0.0
			lEn = 0.0
			lLn = 0.0
		else :
			hHn = high(nDayHighList)
			hEn = high(nDayEndList)
			lEn = low(nDayEndList)
			lLn = low(nDayLowList)

		range_1 = hHn - lEn
		range_2 = hEn - lLn
		if range_1 > range_2 :
			range_f = range_1
		else :
			range_f = range_2
		buyPrice = row[i_open] + Ks * range_f
		sellPrice = row[i_open] - Kx * range_f

		row.append(buyPrice)
		row.append(sellPrice)

		nDayHighList.append(row[i_high])
		nDayEndList.append(row[i_end])
		nDayLowList.append(row[i_low])
		if len(nDayEndList) > tN:
			del nDayHighList[0]
			del nDayEndList[0]
			del nDayLowList[0]

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
