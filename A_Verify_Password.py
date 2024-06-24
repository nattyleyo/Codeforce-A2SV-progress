
t= int(input())
for _ in range(t):
    n = int(input())
    p = input()
    num = set(['0','1','2','3','4','5','6','7','8','9'])
    flag = True
    tmp = ''.join(sorted(p))
    
    
    for i in range(1,n):
        if p[i-1] not in num and p[i] in num:
            flag = False
            break
    # print(flag,p,tmp)
    if flag and tmp == p:
        print('YES')
    else:
        print('NO')
            