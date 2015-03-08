import sqlite3
import config 
def writeToDB(dbFile, tbl, values):

	print(dbFile)
	print(tbl)

	drp_tb_sql = "drop table if exists " + tbl
	crt_tb_sql = config.getTblSql(tbl)

	con = sqlite3.connect(dbFile)
	cur = con.cursor()
	 
	cur.execute(drp_tb_sql)
	cur.execute(crt_tb_sql)

	 

	insert_sql = "insert into "+tbl+" values "

	for row in values:
		in_sql = insert_sql+row
		# print(in_sql)
		cur.execute(in_sql)
	 
	con.commit()
	 
	cur.close()
	con.close()

# test ================
if __name__=='__main__':
	writeToDB("/Users/xiaofuan/Documents/workplace/project/Slots/lua/resources/res/storage/mydatabase.sqlite","tbl_LevelCLTable",['(1.0,1.5,1.45,1.4,1.35,1.3,1.25,1.2,1.15,1.1,1.05)', '(2.0,1.47,1.42,1.37,1.32,1.27,1.224,1.178,1.132,1.086,1.04)'] )