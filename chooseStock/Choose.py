import rfsqlite
import config
import getname
import w2sqlite
import dataAnalyze
import summarize
import datetime

if __name__=='__main__':

	testMode = config.getTestMode()

	if testMode:
		rFile = config.getTestProDatabaseName()

		rAnaFile = config.getTestAnaDatabaseName()

		wFile = config.getTestChooseDatabaseName()
		sumFile = config.getTestSumDatabaseName()

		path = config.getTestCSVFilePath()
	else :
		rFile = config.getProDatabaseName()

		rAnaFile= config.getAnaDatabaseName()

		wFile = config.getChooseDatabaseName()
		sumFile = config.getSumDatabaseName()

		path = config.getCSVFilePath()

	flagStr = config.getFlagStr()
	kind = "Choose"

	tblList = getname.getTblList(path, flagStr)
	totalChoose = []


	#read Data from AnaDatabase
	totalTblDict = {}
	for tbl in tblList:
		print(tbl)
		anaData = rfsqlite.getDataFromDB(rAnaFile, tbl)
		#print(anaData)
		singleAnaData = []
		if anaData:
			singleAnaData = anaData[-1]
			if singleAnaData[0] == 0:
				singleAnaData = anaData[-2]
				if singleAnaData == anaData[0]:
					singleAnaData = []
				else :
					singleAnaData = anaData[-3]
		totalTblDict[tbl] = singleAnaData
	#read Data END

	time_begin = datetime.datetime.now()
	print(time_begin)

	for tbl in tblList:

		print(tbl)		

		data = rfsqlite.getDataFromDB(rFile, tbl)

		singleChoose = []#code, buy_Price, sell_Price, rate
		if data:
			singleChoose = dataAnalyze.chooseQstock(data, tbl)

		if singleChoose:
			chooseAnaData = totalTblDict.get(tbl)

			oriRateTime = 0.0
			time = 0
			level = -10
			if chooseAnaData:
				oriRateTime = chooseAnaData[7]
				time = chooseAnaData[6]
			# if oriRateTime >= 0.6 & time >= 6:
			# 	level = 5
			# elif (oriRateTime >= 0.3 & time >= 6) || (oriRateTime >= 0.6 & time >= 3):
			# 	level = 4
			# elif (oriRateTime >= 0.3 & time >= 3) || (oriRateTime >= 0.6 & time >= 1):
			# 	level = 3
			# elif (oriRateTime > 0.0 & time >= 1):
			# 	level = 2
			# elif :
			# 	level = 1

			singleChoose.append(oriRateTime)
			singleChoose.append(time)
			# singleChoose.append(level)

			totalChoose.append(singleChoose)

	w2sqlite.writeToDB(wFile, tbl, kind, totalChoose)

	time_end = datetime.datetime.now()
	time_dur = time_end - time_begin
	print(time_begin)
	print(time_end)
	print(time_dur)