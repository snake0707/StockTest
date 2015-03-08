import xlrd

def formateRow(row):
	ret = "("
	for i in range(len(row)):
		ret = ret + "'" + str(row[i]) + "'"
		if i != len(row)-1:
			ret = ret + ","
	ret = ret + ")"

	return ret


def getDataFromXls(xlsFilePath):
	workBook = xlrd.open_workbook(xlsFilePath)

	data = {}

	for name in workBook.sheet_names():
		table = workBook.sheet_by_name(name)
		rows = []
		rowNum = table.nrows
		rowList = table.row_values
		for i in range(rowNum):
			if i != 0: # remove the phrase in table
				rows.append(formateRow(rowList(i)))
		# print(rows)
		data[name] = rows

		# print(name+"==========================")
		# print(data[name])



	return data

# test ================
if __name__=='__main__':
	rowsInSheets = getDataFromXls('data.xlsx')
	for k, v in rowsInSheets.items():
		print(k)