n = int(input())
ans = 0
for i in range(6,n+1):
    fact = set()
    d = 2
    while d*d <= i:
        while i%d == 0:
            fact.add(d)
            i //= d
        d += 1
    if i > 1:
        fact.add(i)
    if len(fact) == 2:
        ans += 1
print(ans)
    
        