from collections import defaultdict

def divisors(N):
    div = [[] for _ in range(N)]
    for i in range(1, N):
        for j in range(i, N, i):
            div[j].append(i)
    for i in range(1, N):
        div[i].sort(reverse=True)
    return div



t = int(input())
res = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    N = max(a)
    div = divisors(N+1)
    a.sort()
    
    ans = 0
    k = n
    
    cnt = defaultdict(int)
    
    for e in a:
        k -= 1
        tmp = defaultdict(int)
        
        for d in div[e]:
            val = cnt[d] - tmp[d]
            
            for d2 in div[d]:
                tmp[d2] += val
            
            ans += d * val * k
        
        for d in div[e]:
            cnt[d] += 1
    
    res.append(ans)

for i in res:
    print(i)
