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
		wFile = config.getTestAnaDatabaseName()
		sumFile = config.getTestSumDatabaseName()

		path = config.getTestCSVFilePath()
	else :
		rFile = config.getProDatabaseName()
		wFile = config.getAnaDatabaseName()
		sumFile = config.getSumDatabaseName()

		path = config.getCSVFilePath()

	flagStr = config.getFlagStr()
	kind1 = "Ana"
	kind2 = "Sum"

	tblList = getname.getTblList(path, flagStr)
	moveList = []
	sumList = []

	time_begin = datetime.datetime.now()
	print(time_begin)

	for tbl in tblList:

		print(tbl)		

		data = rfsqlite.getDataFromDB(rFile, tbl)
		#moveList = dataAnalyze.ana(data)
		#print(moveList)
		#moveList = dataAnalyze.anaDonchian(data)
		#moveList = dataAnalyze.anaDonAndDual(data)
		moveList = dataAnalyze.anaSS_1(data)

		if len(moveList) % 2 == 1:
			moveList.pop()

		sumList = summarize.sum(tbl, moveList)

		w2sqlite.writeToDB(wFile, tbl, kind1, moveList)
		w2sqlite.writeToDB(sumFile, tbl, kind2, sumList)

	time_end = datetime.datetime.now()
	time_dur = time_end - time_begin
	print(time_begin)
	print(time_end)
	print(time_dur)