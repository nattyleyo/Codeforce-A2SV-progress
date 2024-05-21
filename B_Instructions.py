test = int(input())

for _ in range(test):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0] * n
    for i in range(n-1, -1, -1):
        if i + a[i] >= n:
            dp[i] = a[i]
        else:
            dp[i] = a[i] + dp[i + a[i]]
  
    print(max(dp))