from math import ceil
t = int(input())
for _ in range(t):
    n,s = list(map(int,input().split()))
    m = (n//2)+1
    
    print(s // m)