from collections import defaultdict
t = int(input())
for _ in range(t):
    s = list(input())
    tmp = s[::]
    tmp.reverse()
    ans = s+tmp
    print(''.join(ans))