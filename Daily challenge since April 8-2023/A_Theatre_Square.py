from math import ceil
n,m,a = list(map(int,input().split()))
ans = ceil(n/a) * ceil(m/a)
print(ans)