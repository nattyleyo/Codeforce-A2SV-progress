from bisect import bisect_right
s,b = list(map(int,input().split()))
ships = list(map(int, input().split()))
bases = []
res = []
for _ in range(b):
    d,g = list(map(int, input().split()))
    bases.append((d,g))
    res.append(d)
bases.sort()
res.sort()
pref = [0]*b
pref[0] = bases[0][1]
for i in range(1,b):
    pref[i] = pref[i-1] + bases[i][1]
ans = ''
for i in range(s): 
    pos = bisect_right(res,ships[i])
    if pos:
        print(pref[pos-1],end=' ')
    else:
        print(0,end=' ')
        