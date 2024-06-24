from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    ans = a[0]
    for i in range(1,n):
        ans &= a[i]
    print(ans)
    
    