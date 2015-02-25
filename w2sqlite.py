import sqlite3
import csv
import config

def isTblExists(dbFile, tbl):
	flag = False
	find_tal_sql = "select name from sqlite_master"
	con = sqlite3.connect(dbFile)
	cur = con.cursor()
	cur.execute(find_tal_sql)
	tblNameList = cur.fetchall()

	for name in tblNameList:
		if tbl in name:
			flag = True
			break
	
	cur.close()
	con.close()
	return flag

def createTbl(dbFile, tbl, tblStruct):
	con = sqlite3.connect(dbFile)
	cur = con.cursor()

	crt_tb_sql = "create table if not exists " + tbl + tblStruct
	cur.execute(crt_tb_sql)
	con.commit()

	cur.close()
	con.close()

def dropTbl(dbFile, tbl):
	con = sqlite3.connect(dbFile)
	cur = con.cursor()

	drp_tb_sql = "drop table if exists " + tbl
	cur.execute(drp_tb_sql)
	con.commit()

	cur.close()
	con.close()

def insertTbl(dbFile, tbl, values):
	con = sqlite3.connect(dbFile)
	cur = con.cursor()

	insert_sql = "insert into " + tbl + " values "

	for row in values:
		strrow = map(str, row)
		#print(row)
		#print(strrow)
		rec = "("
		for i in range(0, len(strrow)):
			#print(row[i])
			#print(strrow[i])
			rec = rec + "'" + strrow[i] + "'"
			if i < len(strrow) - 1:
				rec += ", "
		rec += ")"
		in_sql = insert_sql + rec
		cur.execute(in_sql)

	con.commit()
	 
	cur.close()
	con.close()

#def createDB(dbFile, tbl, values = []):

#	print(dbFile)
#	print(tbl)

#	oriTblStruct = config.getOriTblStruct()

#	if not isTblExists(dbFile, tbl):
#		createTbl(dbFile, tbl, oriTblStruct)

#	insertTbl(dbFile, tbl, values)

#def writeToDB(dbFile, tbl, values = []):

#	print(dbFile)
#	print(tbl)

#	proTblStruct = config.getProTblStruct()

#	dropTbl(dbFile, tbl)
#	createTbl(dbFile, tbl, proTblStruct)

#	insertTbl(dbFile, tbl, values)

def writeToDB(dbFile, tbl, kind, values = []):
	#print(dbFile)
	#print(tbl)

	if kind == "CAW":
		tblStruct = config.getOriTblStruct()

		if not isTblExists(dbFile, tbl):
			createTbl(dbFile, tbl, tblStruct)

		insertTbl(dbFile, tbl, values)
	elif kind == "ProMA":
		tblStruct = config.getProMATblStruct()

		dropTbl(dbFile, tbl)
		createTbl(dbFile, tbl, tblStruct)

		insertTbl(dbFile, tbl, values)
	elif kind == "ProKDJ":
		tblStruct = config.getProKDJTblStruct()

		dropTbl(dbFile, tbl)
		createTbl(dbFile, tbl, tblStruct)

		insertTbl(dbFile, tbl, values)
	elif kind == "ProDonchian":
		tblStruct = config.getProDonchianTblStruct()

		dropTbl(dbFile, tbl)
		createTbl(dbFile, tbl, tblStruct)

		insertTbl(dbFile, tbl, values)
	elif kind == "Ana":
		tblStruct = config.getAnaTblStruct()

		dropTbl(dbFile, tbl)
		createTbl(dbFile, tbl, tblStruct)

		insertTbl(dbFile, tbl, values)
	elif kind == "Sum":
		tblStruct = config.getSumTblStruct()

		#dropTbl(dbFile, tbl)
		#createTbl(dbFile, tbl, tblStruct)
		sumTbl = config.getSumTblName()
		if not isTblExists(dbFile, sumTbl):
			createTbl(dbFile, sumTbl, tblStruct)

		insertTbl(dbFile, sumTbl, values)

# test ================
if __name__=='__main__':
	values = csv.reader(file("SH1A0003.csv","rb"))
	#for line in values:
	#	for data in line:
	#		print(data)
	creatDB("test_read001.db", "SH1A0003", values)