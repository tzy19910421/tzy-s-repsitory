import os
num = int(input('请输入需要的文件加个数:'))
for i in range(0,num):
    os.mkdir(f'./{i+1}')
