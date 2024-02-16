t = int(input())
for i in range(t):
    noiceStr = input()
    m = len(noiceStr)
    my_set = set()
    my_set = {'Y', 'e', 's'}
    flag = True
    if m <= 1 and noiceStr[0] not in my_set:
        flag = False
    for p in range(m-1):
        if noiceStr[p] == 'Y' and noiceStr[p+1] == 'e':
            flag = True
        elif noiceStr[p] == 'e' and noiceStr[p+1] == 's':
            flag = True
        elif noiceStr[p] == 's' and noiceStr[p+1] == 'Y':
            flag = True
        else:
            flag = False
            break
    if flag == True:
        print('YES')
    else:
        print('NO')
