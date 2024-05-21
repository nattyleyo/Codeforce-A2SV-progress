n, a, b, c = list(map(int, input().split()))
dp = [float('-inf')] * (n+1)
dp[0] = 0
s = set([a,b,c])
for i in range(1, n+1):
    for k in s:
        if k <= i:
            rem = i-k
            x = 1+dp[rem]
            dp[i] = max(dp[i],x)
print(dp[n])