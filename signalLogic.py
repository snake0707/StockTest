import config
import datetime

def isbuy(row):
	singleBuyTag = False
	totalBuyTag = True

	i_MA5 = config.getMA5Num()
	i_MA10 = config.getMA10Num()

	#i_K = config.getKNum()
	#i_D = config.getDNum()

	if row[i_MA5] > row[i_MA10]:
	#if row[i_K] > row[i_D]:
		singleBuyTag = True
		#print("buy")

	return (singleBuyTag and totalBuyTag)

def buyDonPrice(row):
	singleBuyTag = False
	totalBuyTag = True

	singleBuyPrice = 0.0

	i_CurHigh = config.getHighNum()
	i_HighN = config.getHignNNum()
	if row[i_CurHigh] > row[i_HighN]:
		ingleBuyTag = True
		singleBuyPrice = row[i_HighN]

	#return (singleBuyTag and totalBuyTag)
	return singleBuyPrice

def sellDonPrice(row, lastBuy):
	singleSellTag = False
	totalSellTag = True
	winStopTag = False
	loseStopTag = False
	dateSellTag = False

	singleSellPrice = 0.0

	i_LowN = config.getLowNNum()
	i_CurLow = config.getLowNum()
	if row[i_CurLow] < row[i_LowN]:
		singleSellTag = True
		singleSellPrice = row[i_LowN]
		return singleSellPrice

	i_CurHigh = config.getHighNum()
	i_lastBuyPrice = config.getLastBuyPrice()
	winStopPrice = lastBuy[i_lastBuyPrice] * (1 + config.getWinStopRate())
	loseStopPrice = lastBuy[i_lastBuyPrice] * (1 - config.getLoseStopRate())
	if row[i_CurHigh] > winStopPrice:
		winStopTag = True
		singleSellPrice = winStopPrice
		return singleSellPrice
	if row[i_CurLow] < loseStopPrice:
		loseStopTag = True
		singleSellPrice = loseStopPrice
		return singleSellPrice

	i_curDate = config.getDateNum()
	curDateStr = row[i_curDate]
	curYear = int(curDateStr[0:4])
	curMonth = int(curDateStr[5:7])
	curDay = int(curDateStr[8:])
	curDate = datetime.datetime(curYear, curMonth, curDay)
	i_lastBuyDate = config.getLastBuyDate()
	lastBuyDateStr = lastBuy[i_lastBuyDate]
	lastBuyYear = int(lastBuyDateStr[0:4])
	lastBuyMonth = int(lastBuyDateStr[5:7])
	lastBuyDay = int(lastBuyDateStr[8:])
	lastBuyDate = datetime.datetime(lastBuyYear, lastBuyMonth, lastBuyDay)

	if (curDate - lastBuyDate).days > config.getHoldDays():
		dateSellTag = True
		i_curPrice = config.getEndNum()
		singleSellPrice = row[i_curPrice]
		return singleSellPrice

	#return ((singleSellTag and totalSellTag) or winStopTag or loseStopTag or dateSellTag)
	return singleSellPrice

def issell(row, lastBuy):
	singleSellTag = False
	totalSellTag = True
	winStopTag = False
	loseStopTag = False
	dateSellTag = False

	#print(lastBuy)

	i_MA5 = config.getMA5Num()
	i_MA10 = config.getMA10Num()

	#i_K = config.getKNum()
	#i_D = config.getDNum()

	if row[i_MA5] < row[i_MA10]:
	#if row[i_K] < row[i_D]:
		singleSellTag = True
		#print("singleSellTag")

	i_curPrice = config.getEndNum()
	i_lastBuyPrice = config.getLastBuyPrice()
	winStopPrice = lastBuy[i_lastBuyPrice] * (1 + config.getWinStopRate())
	loseStopPrice = lastBuy[i_lastBuyPrice] * (1 - config.getLoseStopRate())

	if row[i_curPrice] > winStopPrice:
		winStopTag = True
		#print("winStopTag")
	if row[i_curPrice] < loseStopPrice:
		loseStopTag = True
		#print("loseStopTag")

	i_curDate = config.getDateNum()
	curDateStr = row[i_curDate]
	curYear = int(curDateStr[0:4])
	curMonth = int(curDateStr[5:7])
	curDay = int(curDateStr[8:])
	curDate = datetime.datetime(curYear, curMonth, curDay)
	i_lastBuyDate = config.getLastBuyDate()
	lastBuyDateStr = lastBuy[i_lastBuyDate]
	lastBuyYear = int(lastBuyDateStr[0:4])
	lastBuyMonth = int(lastBuyDateStr[5:7])
	lastBuyDay = int(lastBuyDateStr[8:])
	lastBuyDate = datetime.datetime(lastBuyYear, lastBuyMonth, lastBuyDay)
	#print(curDate - lastBuyDate).days

	#holdDays = int((curDate - lastBuyDate).days)

	if (curDate - lastBuyDate).days > config.getHoldDays():
		dateSellTag = True
		#print("dateSellTag")
	#date_test = "2000/10/10"
	#date = row[i_curDate] - date_test
	#print(curDate).day
	#print((singleSellTag and totalSellTag) or winStopTag or loseStopTag or dateSellTag)

	return ((singleSellTag and totalSellTag) or winStopTag or loseStopTag or dateSellTag)