t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    nums = [i for i in range(1, k+1) if i != x]
    nums.reverse()
    comb = []
    
    Sum = 0
    for x in nums:
        while Sum + x <= n:
            comb.append(x)
            Sum += x
            if Sum == n:
                break
        if Sum == n:
            break
    
    if Sum == n:
        print("YES")
        print(len(comb))
        print(*comb)
    else:
        print("NO")
