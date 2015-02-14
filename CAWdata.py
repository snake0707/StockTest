import getname
import w2sqlite
import csv
import config
import datetime

if __name__=='__main__':

	wFile = config.getOriDatabaseName()
	path = config.getCSVFilePath()
	flagStr = config.getFlagStr()
	tblNameDict = getname.getFileDict(path, flagStr)
	kind = "CAW"

	time = datetime.datetime.now()
	print(time)

	for filePath, tbl in tblNameDict.items():
		values = csv.reader(file(filePath,"rb"))
		w2sqlite.writeToDB(wFile, tbl, kind, values)

		print(tbl)

	time = datetime.datetime.now()
	print(time)

	#print(processed_data)
