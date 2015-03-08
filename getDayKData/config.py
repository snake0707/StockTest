import os

def getCSVFilePath():
	path = os.getcwd() + "/csv"
	return path

def getTestCSVFilePath():
	path = os.getcwd() + "/csvTest"
	return path

def getStockCodeDatabaseName():
	stockCodeDatabaseName = "SHZZStockCode.db"
	return stockCodeDatabaseName

def getBeginDate():
	beginDate = "2012/01/01"
	return beginDate

def getEndDate():
	endDate = "2020/01/01"
	return endDate

def getFlagStr():
	flagStr = ".csv"
	return flagStr