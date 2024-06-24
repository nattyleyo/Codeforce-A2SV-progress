t = int(input())
results = []

for _ in range(t):
    n = int(input().strip())
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(input().strip())
    
    ps = [0] * (n + 1)
    for i in range(1, n + 1):
        ps[i] = ps[i - 1] + a[i]
    
    q = int(input().strip())
    res = []
    for _ in range(q):
        l, u = map(int, input().strip().split())
        
        lb, rb = l, n
        while lb < rb:
            mid = (lb + rb + 1) // 2
            if ps[mid] - ps[l - 1] <= u:
                lb = mid
            else:
                rb = mid - 1
        
        maxu = -1e18
        optid = -1
        for i in range(max(l, lb - 2), min(n, lb + 2) + 1):
            t = ps[i] - ps[l - 1]
            ut = (u + (u - t + 1)) * t / 2
            if ut > maxu:
                maxu = ut
                optid = i
        
        res.append(optid)
    results.append(res)

for res in results:
    print(" ".join(map(str, res)))
