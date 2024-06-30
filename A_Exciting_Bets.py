t = int(input())


for _ in range(t):
    a, b = map(int, input().split())
    
    if a == b:
        print(0, 0)
    else:
        g = abs(a - b)
        m = min(a % g, g - a % g)
        print(g, m)
