def divisors(n):
    f = set()
    d = 2
    while d*d <= n:
        while n%d == 0:
            f.add(d)
            if n//d !=1:
                f.add(n//d)
            n //= d
        d += 1
    return f

n = int(input())
a = list(map(int,input().split()))
m = a[-1]
dp = [0]*(m+1)

        
for x in a:
    d = divisors(x)
    dp[x] = 1
    for c in d:
        dp[x] = max(dp[x],dp[c]+1)
    for c in d:
        dp[c] = max(dp[c],dp[x])
    # print(x,d,p)
print(max(dp))