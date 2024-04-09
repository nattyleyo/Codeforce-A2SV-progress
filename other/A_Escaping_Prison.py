test = int(input())
for _ in range(test):
    n , h = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        w,l = list(map(int,input().split()))
        ans += max(w,l)
    if ans >= h:
        print('YES')
    else:
        print('NO')