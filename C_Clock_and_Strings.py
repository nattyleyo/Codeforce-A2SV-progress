from collections import defaultdict
test = int(input())
for _ in range(test):
    a,b,c,d = list(map(int,input().split()))
    flag = True
    up = {i for i in range(min(a,b),max(a,b)+1)}
    low = set()
    for i in range(1,13):
        if i not in up:
            low.add(i)
    # print(up,low)
    if c in up and d in low:
        flag = False
    if d in up and c in low:
        flag = False
    
    if not flag:
        print('YES')
    else:
        print('NO')
