from collections import defaultdict
test = int(input())
for _ in range(test):
    s = list(input())
    x = ''.join(s)
    n = len(s)
    for i in range(n-1):
        s[i],s[i+1] = s[i+1],s[i]
    ans = ''.join(s)
    if ans != x:
        print('YES')
        print(ans)
    else:
        print('NO')