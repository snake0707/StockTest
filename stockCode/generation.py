import rfxlsx
import w2sqlite

if __name__=='__main__':

	xlsxFile = "SHZZStockCode.xlsx"
	dbFile = "SHZZStockCode.db"

	data = rfxlsx.getDataFromXls(xlsxFile)

	for k, v in data.items():
		w2sqlite.writeToDB(dbFile, k, v)
