num = input().split()
x = int(num[0])
y = float(num[1])
print(num[1]) if x > y - 0.5 or x % 5 != 0 else print('{0:.2f}'.format(y - x - 0.50))
