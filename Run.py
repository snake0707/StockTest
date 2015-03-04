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

	flagStr = config.getFlagStr()
	kind = "Result"

	tblList = getname.getTblList(path, flagStr)
	moveList = []
	sumList = []

	defaultTbl = config.getDefaultTbl()
	listName = "date"
	dateList = rfsqlite.getListFromDB(rFile ,defaultTbl, listName)

	resultList =[]
	defaultResult = [0, 0, 100000, 100000, 10, 10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "init", 0, 0, 0]
	resultList.append(defaultResult)

	totalTblDict = {}
	singleTblDict = {}
	for tbl in tblList:
		data = rfsqlite.getDataFromDB(rFile, tbl)
		for singleData in data:
			#print(singleData)
			curDate = singleData[0]
			#singleTblDict = {curDate: singleData}
			singleTblDict[curDate] = singleData
			print(curDate)
			print(singleTblDict)
		#totalTblDict = {tbl: singleTblDict}
		totalTblDict[tbl] = singleTblDict
		#print(totalTblDict)


	time_begin = datetime.datetime.now()
	print("time begin:")
	print(time_begin)

	for date in dateList:
		buyOptList =[]
		singleDate = date[0]
		print(singleDate)
		#for Result in resultList:
		#	print(Result)
		for tbl in tblList:
			dataList = rfsqlite.getDataFromDBOnDate(rFile, tbl, singleDate)
			
			if dataList:
				data = dataList[0]
				#print(data)

				if data[1] == "sell":
					sellResult = action.sellAction(data, tbl, resultList, singleDate)
					if sellResult:
						resultList.append(sellResult)
				else :
					#buyOpt = action.buyOption(data, tbl)
					buyOpt = list(data)
					buyOpt.append(tbl)
					buyOptList.append(buyOpt)
					#print(buyOpt)
					#print(buyOptList)
				
		if buyOptList:
			#print(buyOptList)
			action.buyAction(buyOptList, resultList, singleDate)
			#buyResultList = action.buyAction(buyOptList, resultList, singleDate)
		#if buyResultList:
			#for buyResult in buyResultList:
				#resultList.append(buyResult)

		

	w2sqlite.writeToDB(wFile, tbl, kind, resultList)

	time_end = datetime.datetime.now()
	time_dur = time_end - time_begin
	print(time_begin)
	print(time_end)
	print(time_dur)