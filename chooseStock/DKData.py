#---------------------------------import---------------------------------------
import urllib2
import csv
import time
import datetime
import rfsqlite
import config
import os
import getname
from collections import Iterable

#------------------------------------------------------------------------------
def outDayKCsv(code, place, day, seconds = u"86400"):
    #userMainUrl = "http://www.google.com/finance/getprices?q=000001&x=SHA&i=86400&p=2d&f=d,c,v,o,h,l";
    userMainUrl = "http://www.google.com/finance/getprices?q=" + code + "&x=" + place + "&i=" + seconds + "&p=" + day + "&f=d,c,v,o,h,l";
    #print(userMainUrl)
    print(code, place)
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    #print "respHtml=",respHtml; # you should see the ouput html
    tableStr = respHtml[196:]
    tableList = tableStr.split('\n')
    #print(tableList)

    dataList = []
    #0:date		1:close		2:high		3:low		4:open		5:volume
    for row in tableList:
    	singleList = row.split(',')
    	dataList.append(singleList)
    
    dataList.pop()
    if dataList:
        firstData = dataList[0]

    pDataList = []
    #0:date 	1:open		2:high		3:low		4:close		5:volume	6:tVolume
    for singleList in dataList:
    	#print(singleList)
    	pSingleList = []
    	if singleList == firstData:
    		date = time.strftime("%Y/%m/%d", time.gmtime(float(firstData[0])))
    	else :
    		date = time.strftime("%Y/%m/%d", time.gmtime(float(firstData[0]) + float(singleList[0]) * 86400))
    	openData = float(singleList[4])
    	highData = float(singleList[2])
    	lowData = float(singleList[3])
    	closeData = float(singleList[1])
    	volumeData = float(singleList[5])
    	tVolumeData = 0.0
    	pSingleList = [date, openData, highData, lowData, closeData, volumeData, tVolumeData]
    	pDataList.append(pSingleList)

    csvFilePath = config.getCSVFilePath()
    flag = config.getFlagStr()
    fileName = place + code + flag
    csvFileName = os.path.join(csvFilePath, fileName)
    with open(csvFileName, 'a+') as csvfile:
    	writer = csv.writer(csvfile)
    	for singleList in pDataList:
    		writer.writerow(singleList)
    		

###############################################################################
if __name__=="__main__":
    rFile = config.getStockCodeDatabaseName()
    tbl = "stock"

    #day = "6M"
    #daily update
    day = "1d"
    #code = u"000001"
    #place = "SHA"
    #print(code)
    #outDayKCsv(code, place, day)

    #print(time.clock())
    #time.sleep(10)
    #print(time.clock())

    #path = config.getCSVFilePath()
    #flagStr = config.getFlagStr()

    #codeList = getname.getTblList(path, flagStr)
    #print(codeList)
    codeList = rfsqlite.getDataFromDB(rFile, tbl)
    #print(codeList)

    time_begin = datetime.datetime.now()
    print(time_begin)

    for singleCodeList in codeList:
        codeStr = singleCodeList[0]
        code = codeStr[3:]
        place = codeStr[:3]
        #print(code)
        #print(place)
        outDayKCsv(code, place, day)
        time.sleep(0.1)


    #print(codeList[0])
    print(code)
    #outDayKCsv(code, place, day)

    time_end = datetime.datetime.now()
    time_dur = time_end - time_begin
    print(time_begin)
    print(time_end)
    print(time_dur)



















