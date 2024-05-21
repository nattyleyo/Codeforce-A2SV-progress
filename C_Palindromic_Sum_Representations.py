mod = 10**9 + 7
maxi = 4*(10**4) 
coin = [i for i in range(1,maxi+1) if str(i) == str(i)[::-1]]        
dp = [0]*(maxi+1)
dp[0] = 1

for c in coin:
    for i in range(c,maxi+1):
        if c <= i:
            r = i-c
            dp[i] = (dp[i] + dp[r])%mod
# print(dp[:13])        
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n]%mod)
    
    