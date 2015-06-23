import os

def isSubString(subStringList, str):
	flag = False
	for substr in subStringList:
		if substr in str:
			flag = True
			break
	return flag

def getTblList(path, flagStr = []):
	fileDict = getFileDict(path, flagStr)
	tblList = []

	for tbl in fileDict.values():
		if tblList.count(tbl) == 0:
			tblList.append(tbl)

	return tblList

def getFileDict(path, flagStr = []):
	fileDict = {}
	fileNames = os.listdir(path)

	if len(fileNames) > 0:
		for fn in fileNames:
			fullFileName = os.path.join(path, fn)
			if os.path.isdir(fullFileName):
				subFileDict = getFileDict(fullFileName, flagStr)
				fileDict.update(subFileDict)
			else :
				if len(flagStr) > 0:
					#if isSubString(flagStr, fn):#
					if fn.endswith(flagStr):
						fn_noend = fn[0: len(fn) - len(flagStr)]
						fullFileName = os.path.join(path, fn)
						fileDict[fullFileName] = fn_noend
				else:
					fullFileName = os.path.join(path, fn)
					fileDict[fullFileName] = fn

	return fileDict

# test ===================
if __name__=='__main__':

	path = "/Users/libin/snake/work/python/stock/pastDataAna/csvTest"
	# path = "/Users/oas/Documents/work/slot/tools/sqlite/getname/csv"
	flagStr = '.csv'
	fileDict = getFileDict(path, flagStr)
	tblList = getTblList(path, flagStr)

	print(tblList)
	for tbl, fileName in tblList, fileDict:
		print(tbl, fileName)


	#print(fileDict)
	#for filePath, tbl in fileDict.items():
	#	print(filePath)
	#	print(tbl)
	