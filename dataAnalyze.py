import config
import signalLogic

def sellDon(row, moveList, sellPrice):
	if len(moveList) == 0:
		lastMove = [0, 0, 0, 0, 10000, 0]
	else :
		lastMove = moveList[-1]
	singleMove = []

	curPrice = sellPrice
	rate = curPrice / lastMove[3]
	share = lastMove[2]
	curHold = lastMove[4] + curPrice * share

	singleMove.extend(row[0:1])
	singleMove.append("sell")
	singleMove.append(share) 
	singleMove.append(curPrice)
	singleMove.append(curHold)
	singleMove.append(rate)

	return singleMove

def sell(row, moveList):
	if len(moveList) == 0:
		lastMove = [0, 0, 0, 0, 10000, 0]
	else :
		lastMove = moveList[-1]
	singleMove = []

	#share = config.getDefaultShare()
	curPrice = row[config.getEndNum()]
	rate = curPrice / lastMove[3]
	loseControl = 1 - config.getLoseStopRate()
	winControl = 1 + config.getWinStopRate()
	if rate < loseControl:
		curPrice = lastMove[3] * loseControl
		rate = loseControl
	elif rate > winControl:
		curPrice = lastMove[3] * winControl
		rate = winControl

	share = lastMove[2]
	curHold = lastMove[4] + curPrice * share
	
	singleMove.extend(row[0:1])
	singleMove.append("sell")
	singleMove.append(share)
	singleMove.append(curPrice)
	singleMove.append(curHold)
	singleMove.append(rate)

	return singleMove

def buy(row, moveList):
	if len(moveList) == 0:
		lastMove = [0, 0, 0, 0, 10000, 0]
	else :
		lastMove = moveList[-1]
	singleMove = []

	#share = config.getDefaultShare()
	curPrice = row[config.getEndNum()]
	if curPrice == 0:
		curPrice = row[2]
	share = lastMove[4] / curPrice
	curHold = lastMove[4] - curPrice * share
	rate = 0
	
	singleMove.extend(row[0:1])
	singleMove.append("buy")
	singleMove.append(share)
	singleMove.append(curPrice)
	singleMove.append(curHold)
	singleMove.append(rate)

	return singleMove

def buyDon(row, moveList, buyPrice):
	if len(moveList) == 0:
		lastMove = [0, 0, 0, 0, 10000, 0]
	else :
		lastMove = moveList[-1]
	singleMove = []

	curPrice = buyPrice
	if curPrice == 0:
		curPrice = row[2]
	share = lastMove[4] / curPrice
	curHold = lastMove[4] - curPrice * share
	rate = 0

	singleMove.extend(row[0:1])
	singleMove.append("buy")
	singleMove.append(share)
	singleMove.append(curPrice)
	singleMove.append(curHold)
	singleMove.append(rate)

	return singleMove

def ana(data):
	curdata = map(list, data)
	moveList = []

	#i_MA5 = config.getMA5Num()
	#i_MA10 = config.getMA10Num()

	hold = False

	for row in curdata:
		singleMove = []
		if hold:
			if signalLogic.issell(row, moveList[-1]):
			#if row[i_MA5] < row[i_MA10]:
				singleMove = sell(row, moveList)
				moveList.append(singleMove)
				hold = False
		else :
			if signalLogic.isbuy(row):
			#if row[i_MA5] > row[i_MA10]:
				singleMove = buy(row, moveList)
				moveList.append(singleMove)
				hold = True	

	return moveList

def anaDonchian(data):
	curdata = map(list, data)
	moveList = []

	hold = False

	for row in curdata:
		singleMove = []
		if hold:
			sellPrice = signalLogic.sellDonPrice(row, moveList[-1])
			if sellPrice:
				singleMove = sellDon(row, moveList, sellPrice)
				moveList.append(singleMove)
				hold = False
		else :
			buyPrice = signalLogic.buyDonPrice(row)
			if buyPrice:
				singleMove = buyDon(row, moveList, buyPrice)
				moveList.append(singleMove)
				hold = True	

	return moveList

# test ===================
if __name__=='__main__':

	row = [1,2,3,4,5,6,7,8,9,10]
	moveList = []
	singleMove = buy(row, moveList)
	print(singleMove)
	singleMove = sell(row, moveList)
	print(singleMove)