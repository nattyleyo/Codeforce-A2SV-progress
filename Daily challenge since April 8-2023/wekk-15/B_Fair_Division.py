t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int,input().split()))
    s = sum(c)
    
    if s%2:
        print('NO')
        continue
    a = b= 0
    for i in c:
        if i == 1:
            a+= 1
        else:
            b+= 1
    
    half = s // 2
    # print(a,b,half)
    if half % 2 == 0 or (half % 2 and a > 0):
        print('YES')
    else:
        print('NO')
