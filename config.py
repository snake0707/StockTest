import os

MA5Num = 7

def getTestMode():
	testMode = False
	return testMode

def getCSVFilePath():
	path = os.getcwd() + "/csv"
	return path

def getTestCSVFilePath():
	path = os.getcwd() + "/csvTest"
	return path

def getOriDatabaseName():
	oriDatabaseName = "oriDatabase.db"
	return oriDatabaseName

def getTestOriDatabaseName():
	oriDatabaseName = "oriTestDatabase.db"
	return oriDatabaseName

def getProDatabaseName():
	proDatabaseName = "proMADatabase.db"
	return proDatabaseName

def getTestProDatabaseName():
	proDatabaseName = "proTestMADatabase.db"
	return proDatabaseName

def getAnaDatabaseName():
	anaDatabaseName = "anaMADatabase.db"
	return anaDatabaseName

def getTestAnaDatabaseName():
	anaDatabaseName = "anaTestMADatabase.db"
	return anaDatabaseName

def getSumDatabaseName():
	sumDatabaseName = "sumMADatabase.db"
	return sumDatabaseName

def getTestSumDatabaseName():
	sumDatabaseName = "sumTestMADatabase.db"
	return sumDatabaseName

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

def getMA5Num():
	return MA5Num

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
	return 0.08

def getLoseStopRate():
	return 0.05

def getHoldDays():
	return 5

def getSumTblName():
	sumTblName = "totalSum"
	return sumTblName

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

def getAnaTblStruct():
	anaTblStruct = """(
						date date,
						type text,
						share integer,
						price float,
						total float,
						rate float
						);"""
	return anaTblStruct

def getSumTblStruct():
	sumTblStruct = """(
						type text,
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