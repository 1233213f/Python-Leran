# 时间格式化
import time

# t=time.gmtime()#获取当前时间，表示为计算机可处理的时间格式--格林时间不适合
t = time.localtime(time.time())  # 格式化时间戳time.time()为本地的时间
t1 = time.strftime("%Y-%m-%d %H:%M:%S %p %A", t)  # 格式化时间
print(t1)

timeStr = '2020-08-31 15:15:22 PM Monday'
print(time.strptime(timeStr, "%Y-%m-%d %H:%M:%S %p %A"))  # 表示为计算机可处理的时间格式

start = time.perf_counter()  # 返回一个CPU级别精确时间计数值,一般用于计算时间差
print(start)
time.sleep(1)  # 延时单位1秒
# 计算时间差
end = time.perf_counter()
print("时间差/耗时:"+str(end-start))
