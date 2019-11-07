# 234345456567
#   3  6  9  12
# 三个数一组,从4开始
a = [2, 3, 4]
num = int(input('输入你想得到的数的位数:'))
for i in range(3, num, 3):
    a.extend([a[i - 3] + 1, a[i - 2] + 1, a[i - 1] + 1])
print(a[len(a) - 1])