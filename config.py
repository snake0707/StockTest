import os

MA5Num = 7

def getTestMode():
	testMode = True
	return testMode

def getCSVFilePath():
	path = os.getcwd() + "/csv"
	return path

def getTestCSVFilePath():
	path = os.getcwd() + "/csvTest"
	return path

def getDefaultTbl():
	defaultTbl = "SH1A0001"
	return defaultTbl

def getOriDatabaseName():
	oriDatabaseName = "ori2012-2014Database.db"
	return oriDatabaseName

def getTestOriDatabaseName():
	oriDatabaseName = "ori2010-2011TestDatabase.db"
	return oriDatabaseName

def getProDatabaseName():
	proDatabaseName = "proDon2012-2014Database.db"
	#proDatabaseName = "proDual2012-2014Database.db"
	return proDatabaseName

def getTestProDatabaseName():
	proDatabaseName = "pro2010-2011TestDonDatabase.db"
	#proDatabaseName = "proTestDualDatabase.db"
	return proDatabaseName

def getAnaDatabaseName():
	anaDatabaseName = "anaDon2012-2014Database.db"
	#anaDatabaseName = "anaDual2012-2014Database.db"
	return anaDatabaseName

def getTestAnaDatabaseName():
	anaDatabaseName = "ana2010-2011TestDonDatabase.db"
	#anaDatabaseName = "anaTestDualDatabase.db"
	return anaDatabaseName

def getSumDatabaseName():
	sumDatabaseName = "sumDon2012-2014Database.db"
	#sumDatabaseName = "sumDual2012-2014Database.db"
	return sumDatabaseName

def getTestSumDatabaseName():
	sumDatabaseName = "sum2010-2011TestDonDatabase.db"
	#sumDatabaseName = "sumTestDualDatabase.db"
	return sumDatabaseName

def getResultDatabaseName():
	resultDatabaseName = "resultDatabase.db"
	return resultDatabaseName

def getTestResultDatabaseName():
	resultDatabaseName = "resultTestDatabase.db"
	return resultDatabaseName

def getBeginDate():
	beginDate = "2012/01/01"
	return beginDate

def getEndDate():
	endDate = "2016/01/01"
	return endDate

def getKDJDay():
	KDJDay = 9
	return KDJDay

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

def getMA5Num():
	return MA5Num

#Don & Dual both use this
def getBuyPriceNum():
	return 7
#Don & Dual both use this
def getSellPriceNum():
	return 8

def getMA10Num():
	return 8

def getKNum():
	return 7

def getDNum():
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
	return 0.2

def getLoseStopRate():
	return 0.05

def getHoldDays():
	return 1000

def getSumTblName():
	sumTblName = "totalSum"
	return sumTblName

def getResultTblName():
	resultTblName = "result"
	return resultTblName

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

def getProMATblStruct():
	proTblStruct = """(
						date date,
						N1 float,
						N2 float,
						N3 float,
						N4 float,
						N5 float,
						N6 float,
						MA5 float,
						MA10 float
						);"""
	return proTblStruct

def getProKDJTblStruct():
	proTblStruct = """(
						date date,
						N1 float,
						N2 float,
						N3 float,
						N4 float,
						N5 float,
						N6 float,
						K float,
						D float,
						J float
						);"""
	return proTblStruct

def getProDonchianTblStruct():
	proTblStruct = """(
						date date,
						N1 float,
						N2 float,
						N3 float,
						N4 float,
						N5 float,
						N6 float,
						hign_n float,
						low_n float
						);"""
	return proTblStruct

def getProDualThrustTblStruct():
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
						share float
						);"""
	return resultTblStruct