t = int(input())
for i in range(t):
    dist = list(map(int, input().split()))
    res = []
    count = 0
    p = 1
    m = len(dist)
    kDist = dist[0]
    while p < m:
        if dist[p] > kDist:
            count += 1
        p += 1
    print(count)
