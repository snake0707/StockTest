import rfsqlite
import config
import getname
import w2sqlite
import dataAnalyze
import summarize
import datetime
import action

if __name__=='__main__':

	testMode = config.getTestMode()

	if testMode:
		rFile = config.getTestAnaDatabaseName()
		wFile = config.getTestResultDatabaseName()

		path = config.getTestCSVFilePath()
	else :
		rFile = config.getAnaDatabaseName()
		wFile = config.getResultDatabaseName()

		path = config.getCSVFilePath()

	dateFile = config.getOriDatabaseName()

	flagStr = config.getFlagStr()
	kind = "Result"

	tblList = getname.getTblList(path, flagStr)
	moveList = []
	sumList = []

	defaultTbl = config.getDefaultTbl()
	listName = "date"
	dateList = rfsqlite.getListFromDB(dateFile ,defaultTbl, listName)

	resultList =[]
	defaultResult = [0, 0, 100000, 100000, 10, 10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "init", 0, 0, 0]
	resultList.append(defaultResult)

	totalTblDict = {}
	singleTblDict = {}

	read_time_begin = datetime.datetime.now()
	print("read_time begin:")
	print(read_time_begin)
	for tbl in tblList:
		print(tbl)
		data = rfsqlite.getDataFromDB(rFile, tbl)
		for singleData in data:
			curDate = singleData[0]
			singleTblDict[curDate] = singleData
		totalTblDict[tbl] = singleTblDict.copy()
		singleTblDict.clear()

	time_begin = datetime.datetime.now()
	print("time begin:")
	print(time_begin)

	for date in dateList:
		buyOptList = []
		sellOptList = []
		singleDate = date[0]
		print(singleDate)
		for tbl in tblList:
			dict1 = totalTblDict[tbl]
			data = dict1.get(singleDate)

			if data:
				if data[1] == "sell":
					sellOpt = list(data)
					sellOpt.append(tbl)
					sellOptList.append(sellOpt)
				else :
					buyOpt = list(data)
					buyOpt.append(tbl)
					buyOptList.append(buyOpt)
				
		if buyOptList:
			action.buyAction(buyOptList, resultList, singleDate)
		if sellOptList:
			for sellOpt in sellOptList:
				sellResult = action.sellAction(sellOpt, resultList, singleDate)
				if sellResult:
					resultList.append(sellResult)

	w2sqlite.writeToDB(wFile, tbl, kind, resultList)

	read_time_dur = time_begin - read_time_begin
	time_end = datetime.datetime.now()
	time_dur = time_end - time_begin
	print("read_time_begin:")
	print(read_time_begin)
	print("read_time_dur:")
	print(read_time_dur)
	print("time_begin:")
	print(time_begin)
	print("time_end: ")
	print(time_end)
	print("time_dur: ")
	print(time_dur)