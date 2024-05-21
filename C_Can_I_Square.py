from collections import defaultdict
test = int(input())
for _ in range(test):
    n = int(input())
    a = list(map(int,input().split()))
    total =sum(a)
    flag = False
    l = 1
    h = total
    while l <= h:
        mid = (l+h)//2
        if mid*mid == total:
            # print('YES')
            flag = True
            break
        elif mid*mid < total:
            l = mid + 1
        else:
            h = mid - 1
    if flag:
        print('YES')
    else:
        print('NO')
    