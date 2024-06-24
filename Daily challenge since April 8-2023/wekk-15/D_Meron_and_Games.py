from collections import Counter
n = int(input())
a = list(map(int,input().split()))
x = Counter(a)
memo = {}
def dp(i,sub):
    if sub < 0:
        return float('-inf')
    if i >= n:
        return 0
    d = 0
    for k in x:
        if k == i+1 or k == i-1:
            d += k*x[k]
    
    if sub > 0:
        return d
    if (i,sub) not in memo:
       
        memo[(i,sub)] = max(dp(i+1,sub+d),dp(i+1,sub))
    return memo[(i,sub)]
print(dp(0,0))
        