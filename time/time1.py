import datetime
import time
 
# 当前时间，得到的是时间戳
now_time = time.time()
# 1543629912.6148438
 
# 当前日期和时间
now_datetime = datetime.datetime.today()
# 2018-12-01 10:05:52.528162
 
# 自定义格式
now_format = '{:%Y-%m-%d %H:%M:%S}'.format(now_datetime)
# 2018-12-01 10:17:2
 
# 设置时间延迟，工程中经常用到
delta_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() - datetime.timedelta(days=10))
# 2018-11-21
 
# 获取10位和13位时间戳
timestamp_10 = int(now_time)
timestamp_13 = int(now_time * 1000)
# 1543630901 1543630901343
 
# 10位时间戳转自定义格式
timeArray=time.localtime(timestamp_10)
otherStyleTime=time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
# 2018-12-01 13:48:18
 
# 13位时间戳转自定义格式
timeArray=time.localtime(timestamp_13/1000)
otherStyleTime=time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
# 2018-12-01 13:48:18
 
# 标准格式转时间戳便于比较
dtime = '2018-12-01 13:48:18'
timeArray = time.strptime(dtime, "%Y-%m-%d %H:%M:%S")
timestamp = time.mktime(timeArray)
# 1543643298.0
 
# 获取今日日期
today = datetime.date.today()
# 2018-12-01
 
# 获取指定日期是星期几，注意星期一是0
weekday = datetime.date.weekday(today)
# 5
 
import random
# sleep方法，加上random贼好用
time.sleep(2*random.random())
