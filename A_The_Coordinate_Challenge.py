t = int(input())
for _ in range(t):
    n = int(input())
    if n%3 == 0:
        ans = n // 3
    elif n%2 == 0:
        ans = n // 3 + 1
    else:
        if n == 1:
            ans = 2
        else:
            ans = (n - 1) // 3 + 1
        
    print(ans)
