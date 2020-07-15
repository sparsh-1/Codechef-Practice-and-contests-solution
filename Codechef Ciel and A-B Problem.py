a, b = map(int, input().split())
res = str(a - b)
if res.startswith('1'):
    rest = '2' + str(res[1:len(res)])
else:
    rest = '1' + str(res[1:len(res)])
print(rest)
