# 文本进度条
import time

scale = 50
start = time.perf_counter()
for i in range(scale + 1):
    a = '*' * i  # 复制i次*
    b = '.' * (scale - i)  # *号加了对应的.就减少
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur, end=''))
    # \r输出一行后换行

# {:^3.0f}--->:引导符 ^居中 3宽度 .代表精度 0f为不取小数位,2f为取2位小数位
#
#

#
#
time.sleep(0.2)
