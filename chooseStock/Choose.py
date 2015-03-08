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
		wFile = config.getTestChooseDatabaseName()
		sumFile = config.getTestSumDatabaseName()

		path = config.getTestCSVFilePath()
	else :
		rFile = config.getProDatabaseName()
		wFile = config.getChooseDatabaseName()
		sumFile = config.getSumDatabaseName()

		path = config.getCSVFilePath()

	flagStr = config.getFlagStr()
	kind = "Choose"

	tblList = getname.getTblList(path, flagStr)
	totalChoose = []

	time_begin = datetime.datetime.now()
	print(time_begin)

	for tbl in tblList:

		print(tbl)		

		data = rfsqlite.getDataFromDB(rFile, tbl)

		singleChoose = []#code, buy_Price, sell_Price, rate
		if data:
			singleChoose = dataAnalyze.chooseQstock(data, tbl)

		if singleChoose:
			totalChoose.append(singleChoose)

	w2sqlite.writeToDB(wFile, tbl, kind, totalChoose)

	time_end = datetime.datetime.now()
	time_dur = time_end - time_begin
	print(time_begin)
	print(time_end)
	print(time_dur)