from collections import defaultdict
test = int(input())
for _ in range(test):
    x,y = list(map(int,input().split()))
    a = min(x,y)
    b = max(x,y)
    print(a,b)