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

def buyDonAndDualPrice(row):
	singleBuyPrice = 0.0

	i_CurHigh = config.getHighNum()
	i_buy = config.getBuyPriceNum()
	if row[i_CurHigh] > row[i_buy]:
		singleBuyPrice = row[i_buy]

	return singleBuyPrice

def buySS_1Price(row, lastNDataList):
	singleBuyPrice = 0.0

	lastDay = config.getSS_1LastDay()

	if len(lastNDataList) < (lastDay - 1):
		return singleBuyPrice

	ma_n = 0.0

	i_high = config.getHighNum()
	i_low = config.getLowNum()
	i_end = config.getEndNum()
	i_buy = config.getBuyPriceNum()
	i_sell = config.getSellPriceNum()

	for data in lastNDataList:
		ma_n = ma_n + data[i_end]
	ma_n = ma_n / len(lastNDataList)

	for data in lastNDataList:
		if ma_n > data[i_high] or ma_n < data[i_low]:
			return singleBuyPrice

	if row[i_low] < row[i_buy] and row[i_high] > row[i_buy]:
		rate = row[i_sell] / row[i_buy]
		if rate >= 1.05:
			singleBuyPrice = row[i_buy]

	return singleBuyPrice

def sellSS_1Price(row, lastBuy):
	singleSellPrice = 0.0

	i_high = config.getHighNum()
	i_low = config.getLowNum()
	i_open = config.getOpenNum()
	i_end = config.getEndNum()
	i_sell = config.getSellPriceNum()

	if row[i_high] > row[i_sell] and row[i_end] < row[i_sell]:
		singleSellPrice = row[i_sell]
		return singleSellPrice

	i_lastBuyPrice = config.getLastBuyPrice()
	winStopPrice = lastBuy[i_lastBuyPrice] * (1 + config.getWinStopRate())
	loseStopPrice = lastBuy[i_lastBuyPrice] * (1 - config.getLoseStopRate())
	if row[i_high] > winStopPrice:
		singleSellPrice = winStopPrice
		return singleSellPrice
	if row[i_low] < loseStopPrice:
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
		i_curPrice = config.getEndNum()
		singleSellPrice = row[i_curPrice]
		return singleSellPrice

	return singleSellPrice

def sellDonAndDualPrice(row, lastBuy):
	singleSellPrice = 0.0

	i_sell = config.getSellPriceNum()
	i_CurLow = config.getLowNum()
	if row[i_CurLow] < row[i_sell]:
		singleSellPrice = row[i_sell]
		return singleSellPrice

	i_CurHigh = config.getHighNum()
	i_lastBuyPrice = config.getLastBuyPrice()
	winStopPrice = lastBuy[i_lastBuyPrice] * (1 + config.getWinStopRate())
	loseStopPrice = lastBuy[i_lastBuyPrice] * (1 - config.getLoseStopRate())
	if row[i_CurHigh] > winStopPrice:
		singleSellPrice = winStopPrice
		return singleSellPrice
	if row[i_CurLow] < loseStopPrice:
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
		i_curPrice = config.getEndNum()
		singleSellPrice = row[i_curPrice]
		return singleSellPrice

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