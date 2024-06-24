from collections import defaultdict,deque
t = int(input())
for _ in range(t):
    x,y,n = list(map(int,input().split()))
    k = (n-y)//x
    ans = k*x + y
    if ans > n:
        ans -= x
    print(ans)