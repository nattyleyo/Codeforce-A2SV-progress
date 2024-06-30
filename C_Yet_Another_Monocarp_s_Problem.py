from collections import Counter
t = int(input())
for _ in range(t):
    n,h = map(int, input().split())
    a = list(map(int,input().split()))
    # print(a)
    low, high = 1, h
    
    while low < high:
        mid = (low+high) // 2
        dam = 0
        for i in range(n-1):
            dam += min(a[i+1] - a[i], mid)
        dam += mid
        
        if dam >= h:
            high = mid
        else:
            low = mid + 1
    print(low)



