# time_module
import time
print(time.time())
print(time.ctime())
t = time.gmtime()
print(t)
print(time.strftime("%Y-%m-%d %H:%M:%S",t))

# 程序计时
start = time.perf_counter()
sum = 0
for i in range(10000000):
    sum = sum + i
time.sleep(1) # 睡眠1s
end = time.perf_counter()
print(end-start)

