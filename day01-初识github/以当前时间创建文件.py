import time
import os
path = input('请输入文件放置的路径,当前路径为(%s):' % os.getcwd())
os.chdir(path)
num = int(input('输入需要的文件数:'))
for i in range(0,num):
    time1 = time.localtime()
    print(time1)
    print(time.strftime('%Y%m%d%H%M%S',time1))
    name = time.strftime('%Y%m%d%H%M%S',time1)+'.txt'
    file = open(name, 'w')
    time.sleep(1)
file.close()