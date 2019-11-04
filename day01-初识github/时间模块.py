import  time
# 格林威治时间
print(time.altzone)
# 返回当前可读字符串
print(time.asctime(),type(time.asctime()))
# print(time.asctime((2013,9,9,9,9,9,9,3,234,1)))
# 代替原有的clock()方法
print(time.process_time())
#和asctime()一样,可以传递时间戳
print(time.ctime(time.time()))
# 返回当前时间戳
print(time.time())
# print(((72870149-14984164)/(60*60*24))%365) #我在看两年前的视频课
# 返回时间元组,时间是格林威治当前时间.
print(time.gmtime())
# 返回当前时间元组
print(time.localtime(),type(time.localtime()))
print('*'*30)
# 1.获取时间戳
time1 = time.time()
print(time1)
# 2.获取时间元组
time2 = time.localtime(time1)
print(time2)
print(type(time2))
# 3.对时间元组进行格式化,字符串格式.
print(time.strftime('%Y/%m/%d %H:%M:%S',time2),type(time.strftime('%Y',time2)))

# 将时间字符串转换为元组,需要给定格式
time_Str = time.strptime('2019-12-12 12:12:12','%Y-%m-%d %H:%M:%S')
print(time_Str)
# 将时间元组转换为时间戳
print(time.mktime(time_Str))

# sleep,推迟线程运行时间
for i in range(1,2):
    print('因为sleep,我运行的有些慢')
    time.sleep(2)
    print('因为sleep,我运行的有些慢')
    time.sleep(2)
    print('因为sleep,我运行的有些慢')