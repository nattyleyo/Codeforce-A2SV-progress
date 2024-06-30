t = int(input())

for _ in range(t):
    x, n, m = map(int, input().split())
    
    while x > 0 and n > 0 and x // 2 + 10 < x:
        n -= 1
        x = x // 2 + 10
    
    if x <= m * 10:
        print("YES")
    else:
        print("NO")
