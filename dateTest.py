import time
import datetime

if __name__=='__main__':

	d1 = datetime.datetime(2015, 1, 22)
	d2 = datetime.datetime(2015, 2, 1)
	print(d1 - d2).days

	time_begin = datetime.datetime.now()
	print(time_begin)

	yourName = raw_input("please input your name: ")
	print(yourName)

	time_end = datetime.datetime.now()
	time_dur = time_end - time_begin
	print(time_begin)
	print(time_end)
	print(time_dur)