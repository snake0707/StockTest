import rfsqlite
import dataprocess
import w2sqlite
import config
import getname
import datetime

if __name__=='__main__':

	rFile = config.getOriDatabaseName()
	wFile = config.getProDatabaseName()
	path = config.getCSVFilePath()
	flagStr = config.getFlagStr()
	kind = "ProMA"
	#kind = "ProKDJ"

	tblList = getname.getTblList(path, flagStr)

	time_begin = datetime.datetime.now()
	print(time_begin)

	for tbl in tblList:

		data = rfsqlite.getDataFromDB(rFile, tbl)

		#MA Pro
		processed_data = dataprocess.processMA(data, 5)
		processed_data = dataprocess.processMA(processed_data, 10)

		#KDJ Pro
		#processed_data = dataprocess.processKDJ(data)

		w2sqlite.writeToDB(wFile, tbl, kind, processed_data)

		print(tbl)

	time_end = datetime.datetime.now()
	time_dur = time_end - time_begin
	print(time_begin)
	print(time_end)
	print(time_dur)
