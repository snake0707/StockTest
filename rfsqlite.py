import sqlite3
import dataprocess

def getDataFromDB(dbFilePath, tbl):
	con = sqlite3.connect(dbFilePath)
	cur = con.cursor()

	sel_tbl = "select * from " + tbl
	rows = cur.execute(sel_tbl)
	res = cur.fetchall()
	
	cur.close()
	con.close()

	return res

def getDataFromDBOnDate(dbFilePath, tbl, date):
	con = sqlite3.connect(dbFilePath)
	cur = con.cursor()

	#sel_tbl_date = "select * from " + tbl + "where 'date' = " + date
	#print(tbl)
	#print(date)
	sel_tbl_date = "select * from " + tbl + " where date = '" + date + "'"
	#print(sel_tbl_date)
	rows = cur.execute(sel_tbl_date)
	res = cur.fetchall()
	
	cur.close()
	con.close()

	return res

def getListFromDB(dbFilePath, tbl, listName):
	con = sqlite3.connect(dbFilePath)
	cur = con.cursor()

	sel_tbl = "select " + listName + " from " + tbl
	rows = cur.execute(sel_tbl)
	res = cur.fetchall()
	
	cur.close()
	con.close()

	return res

# test ===================
if __name__=='__main__':

	rFile = "oriTestDatabase.db"
	tbl = "SH900922"
	date = "2016/12/24"
	listName = "date"
	# wFile = "test_write.db"

	#data = getDataFromDB(rFile, tbl)
	data = getDataFromDBOnDate(rFile, tbl, date)
	#data = getListFromDB(rFile, tbl, listName)

	if not None:
		print(data)
	

	#for singleDate in data:
	#	print(data)

	#processed_data = dataprocess.processMA(data, 5)
	#processed_data = dataprocess.processMA(processed_data, 10)

	#for k in processed_data:
	#	print(k)

	#for k, v in processed_data.items():
	#	print(k)
