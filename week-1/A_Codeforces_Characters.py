str = 'codeforces'
t = int(input())
flag = False
for x in range(t):
    char = input()
    for i in str:
        if char[0] == i:
            flag = True
            break
        else:
            flag = False
    if (flag == True):
        print('YES')
    else:
        print('NO')
