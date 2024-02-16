t = int(input())
flag = False
for x in range(t):
    num = list(map(int, input().split()))
    if (num[0]+num[1] != num[2] and num[0]-num[1] != num[2]) or (num[0]+num[1] != num[2] and num[0]-num[1] == num[2]):
        flag = True
    else:
        flag = False
    if flag == True:
        print('-')
    else:
        print('+')
