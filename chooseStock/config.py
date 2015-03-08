import os

def getTestMode():
	testMode = False
	return testMode

def getCSVFilePath():
	path = os.getcwd() + "/csv"
	return path

def getTestCSVFilePath():
	path = os.getcwd() + "/csvTest"
	return path

def getDefaultTbl():
	defaultTbl = "SHA000001"
	return defaultTbl

def getOriDatabaseName():
	oriDatabaseName = "oriDatabase.db"
	return oriDatabaseName

def getTestOriDatabaseName():
	oriDatabaseName = "oriTestDatabase.db"
	return oriDatabaseName

def getProDatabaseName():
	proDatabaseName = "proDatabase.db"
	return proDatabaseName

def getTestProDatabaseName():
	proDatabaseName = "proTestDatabase.db"
	return proDatabaseName

def getAnaDatabaseName():
	anaDatabaseName = "anaDatabase.db"
	return anaDatabaseName

def getTestAnaDatabaseName():
	anaDatabaseName = "anaTestDatabase.db"
	return anaDatabaseName

def getSumDatabaseName():
	sumDatabaseName = "sumDatabase.db"
	return sumDatabaseName

def getTestSumDatabaseName():
	sumDatabaseName = "sum2TestDatabase.db"
	return sumDatabaseName

def getResultDatabaseName():
	resultDatabaseName = "resultDatabase.db"
	return resultDatabaseName

def getTestResultDatabaseName():
	resultDatabaseName = "resultTestDatabase.db"
	return resultDatabaseName

def getChooseDatabaseName():
	chooseDatabaseName = "choose.db"
	return chooseDatabaseName

def getTestChooseDatabaseName():
	chooseDatabaseName = "chooseTest.db"
	return chooseDatabaseName

def getStockCodeDatabaseName():
	stockCodeDatabaseName = "SHZZStockCode.db"
	return stockCodeDatabaseName

def getBeginDate():
	beginDate = "2014/01/01"
	return beginDate

def getEndDate():
	endDate = "2020/01/01"
	return endDate

def getFlagStr():
	flagStr = ".csv"
	return flagStr

def getDateNum():
	return 0

def getEndNum():
	return 4

def getHighNum():
	return 2

def getLowNum():
	return 3

def getOpenNum():
	return 1

def getBuyPriceNum():
	return 7

def getSellPriceNum():
	return 8

def getDefaultShare():
	return 100

def getPriceNum():
	return 3

def getHoldNum():
	return 4

def getLastBuyPrice():
	return 3

def getLastBuyDate():
	return 0

def getWinStopRate():
	return 1

def getLoseStopRate():
	return 0.05

def getHoldDays():
	return 1000

def getSS_1LastDay():
	return 3

def getSumTblName():
	sumTblName = "totalSum"
	return sumTblName

def getResultTblName():
	resultTblName = "result"
	return resultTblName

def getChooseTblName():
	chooseTblName = "choose"
	return chooseTblName	

def getOriTblStruct():
	oriTblStruct = """(
						date date,
						N1 float,
						N2 float,
						N3 float,
						N4 float,
						N5 float,
						N6 float
						);"""
	return oriTblStruct

def getProSnakeStrategy_1TblStruct():
	proTblStruct = """(
						date date,
						N1 float,
						N2 float,
						N3 float,
						N4 float,
						N5 float,
						N6 float,
						buyPrice float,
						sellPrice float
						);"""
	return proTblStruct

def getAnaTblStruct():
	anaTblStruct = """(
						date date,
						type text,
						share integer,
						price float,
						total float,
						rate float,
						time integer,
						oriRateTime float
						);"""
	return anaTblStruct

def getSumTblStruct():
	sumTblStruct = """(
						code text,
						opeTime integer,
						win integer,
						winRate float,
						lose integer,
						loseRate float,
						rate float,
						mostHold float,
						mostHoldDate date,
						mostBackRate float,
						mostBackRateDate date,
						mostBackHold float,
						mostBackMostHold float,
						mostBackMostHoldDate date
						);"""
	return sumTblStruct

def getChooseTblStruct():
	chooseTblStruct = """(
						code text,
						buyPrice float,
						sellPrice float,
						rate float
						);"""
	return chooseTblStruct

def getResultTblStruct():
	resultTblStruct = """(
						date date,
						opeTime integer,
						totalFund float,
						unuseFund float,
						unusePart integer,
						singleFund float,
						part1Code text,
						part1Price float,
						part1Share float,
						part1Date date,
						part2Code text,
						part2Price float,
						part2Share float,
						part2Date date,
						part3Code text,
						part3Price float,
						part3Share float,
						part3Date date,
						part4Code text,
						part4Price float,
						part4Share float,
						part4Date date,
						part5Code text,
						part5Price float,
						part5Share float,
						part5Date date,
						part6Code text,
						part6Price float,
						part6Share float,
						part6Date date,
						part7Code text,
						part7Price float,
						part7Share float,
						part7Date date,
						part8Code text,
						part8Price float,
						part8Share float,
						part8Date date,
						part9Code text,
						part9Price float,
						part9Share float,
						part9Date date,
						part10Code text,
						part10Price float,
						part10Share float,
						part10Date date,
						type text,
						code text,
						price float,
						share float,
						buydate date
						);"""
	return resultTblStruct