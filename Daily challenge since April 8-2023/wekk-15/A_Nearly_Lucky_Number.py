n = int(input())

count = 0
flag = True
for d in str(n):
    if d == '4' or d == '7':
        count += 1
for d in str(count):
    if d != '4' and d != '7':
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
