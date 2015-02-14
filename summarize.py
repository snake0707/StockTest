import config

def sum(tbl, moveList):
	if len(moveList) < 2:
		return [[tbl, 0, 0, 0, 0, 0, 0]]
	else :
		opetime = len(moveList) / 2
	win = 0
	lose = 0
	rate = 0

	priceNum = config.getPriceNum()

	for i in range(0, opetime):
		buyMove = moveList[i * 2]
		sellMove = moveList[i * 2 + 1]
		if buyMove[priceNum] < sellMove[priceNum]:
			win += 1
		else :
			lose += 1
		rate = sellMove[4] / 10000

	winrate = float(win) / float(opetime)
	loserate = float(lose) / float(opetime)

	sumList = []
	singleList = [tbl, opetime, win, winrate, lose, loserate, rate]
	sumList.append(singleList)

	return sumList