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


# test ===================
if __name__=='__main__':

	rFile = "test_read10.db"
	# wFile = "test_write.db"

	data = getDataFromDB(rFile)

	processed_data = dataprocess.processMA(data, 5)
	processed_data = dataprocess.processMA(processed_data, 10)

	for k in processed_data:
		print(k)

	#for k, v in processed_data.items():
	#	print(k)
