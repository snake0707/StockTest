#---------------------------------import---------------------------------------
import urllib2
import csv
import time
from collections import Iterable

#------------------------------------------------------------------------------
def outDayKCsv(code, place, day, seconds = 86400):
    #userMainUrl = "http://www.google.com/finance/getprices?q=000001&x=SHA&i=86400&p=6M&f=d,c,v,o,h,l";
    userMainUrl = "http://www.google.com/finance/getprices?q=" + code + "&x=" + place + "SHA&i=" + seconds + "&p=" + day + "&f=d,c,v,o,h,l";
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
    firstData = dataList[0]

    pDataList = []
    #0:date 	1:open		2:high		3:low		4:close		5:volume	6:tVolume
    for singleList in dataList:
    	print(singleList)
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

    with open('test.csv', 'wb') as csvfile:
    	writer = csv.writer(csvfile)
    	for singleList in pDataList:
    		writer.writerow(singleList)
    		

###############################################################################
if __name__=="__main__":
    outDayKCsv(code, place, day)