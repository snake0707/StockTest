import rfsqlite
import dataprocess
import w2sqlite
import config
import getname
import datetime

if __name__=='__main__':

	testMode = config.getTestMode()

	if testMode:
		rFile = config.getTestOriDatabaseName()
		wFile = config.getTestProDatabaseName()
		path = config.getTestCSVFilePath()
	else :
		rFile = config.getOriDatabaseName()
		wFile = config.getProDatabaseName()
		path = config.getCSVFilePath()
	
	flagStr = config.getFlagStr()
	#kind = "ProMA"
	#kind = "ProKDJ"
	#kind = "ProDonchian"
	#kind = "ProDualThrust"
	kind = "ProSnakeStrategy_1"

	tblList = getname.getTblList(path, flagStr)

	time_begin = datetime.datetime.now()
	print(time_begin)

	for tbl in tblList:

		data = rfsqlite.getDataFromDB(rFile, tbl)

		#MA Pro
		#processed_data = dataprocess.processMA(data, 5)
		#processed_data = dataprocess.processMA(processed_data, 10)

		#KDJ Pro
		#processed_data = dataprocess.processKDJ(data)

		#Donchian Pro
		#processed_data = dataprocess.processDonchian(data)

		#DualThrust Pro
		#processed_data = dataprocess.processDualThrust(data)

		#SnakeStrategy_1 Pro
		lastDay = config.getSS_1LastDay()
		processed_data = dataprocess.processSnakeStrategy_1(data, lastDay)

		w2sqlite.writeToDB(wFile, tbl, kind, processed_data)

		print(tbl)

	time_end = datetime.datetime.now()
	time_dur = time_end - time_begin
	print(time_begin)
	print(time_end)
	print(time_dur)
