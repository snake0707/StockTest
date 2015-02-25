import config

def sum(tbl, moveList):
	if len(moveList) < 2:
		return [[tbl, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	else :
		opetime = len(moveList) / 2
	win = 0
	lose = 0
	rate = 0

	priceNum = config.getPriceNum()
	holdNum = config.getHoldNum()
	mostHold = 0.0
	mostHoldDate = 0
	mostBackRate = 1.0
	mostBackRateDate = 0
	mostBackHold = 0.0
	mostBackMostHold = 0.0
	mostBackMostHoldDate = 0.0

	for i in range(0, opetime):
		buyMove = moveList[i * 2]
		sellMove = moveList[i * 2 + 1]
		if buyMove[priceNum] < sellMove[priceNum]:
			win += 1
		else :
			lose += 1
		rate = sellMove[4] / 10000

		if mostHold < sellMove[holdNum]:
			mostHold = sellMove[holdNum]
			mostHoldDate = sellMove[0]

		curBackRate = sellMove[holdNum] / mostHold
		if mostBackRate > curBackRate:
			mostBackRate = curBackRate
			mostBackRateDate = sellMove[0]
			mostBackHold = sellMove[holdNum]
			mostBackMostHold = mostHold
			mostBackMostHoldDate = mostHoldDate

	winrate = float(win) / float(opetime)
	loserate = float(lose) / float(opetime)

	sumList = []
	singleList = [tbl, opetime, win, winrate, lose, loserate, rate, mostHold, mostHoldDate, mostBackRate, mostBackRateDate, mostBackHold, mostBackMostHold, mostBackMostHoldDate]
	sumList.append(singleList)

	return sumList