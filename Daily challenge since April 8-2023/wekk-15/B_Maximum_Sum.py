test = int(input())
for _ in range(test):
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    mod = 7+10**9
    s = sum(a)
    x = 0
    for i in range(n):
        s += a[i]
        x += a[i]
    while k >0:
        a.append(s)
        s += s
        k -= 1
    print((s+x)%mod)