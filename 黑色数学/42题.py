sum = 0
for i in range(1, 46):
    sum += i
    if sum % 100 == 0:
        break
print(sum)
print(i)
