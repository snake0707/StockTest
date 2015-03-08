import getname
import w2sqlite
import csv
import config
import datetime

if __name__=='__main__':

	testMode = config.getTestMode()

	if testMode:
		wFile = config.getTestOriDatabaseName()
		path = config.getTestCSVFilePath()
	else :
		wFile = config.getOriDatabaseName()
		path = config.getCSVFilePath()
	
	flagStr = config.getFlagStr()

	tblNameDict = getname.getFileDict(path, flagStr)
	kind = "CAW"

	time_begin = datetime.datetime.now()
	print(time_begin)

	for filePath, tbl in tblNameDict.items():
		values = csv.reader(file(filePath,"rb"))
		w2sqlite.writeToDB(wFile, tbl, kind, values)

		print(tbl)

	time_end = datetime.datetime.now()
	time_dur = time_end - time_begin
	print(time_begin)
	print(time_end)
	print(time_dur)
