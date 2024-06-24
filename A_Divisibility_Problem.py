t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    ans = []
    if a % b == 0:
        ans.append(0)
    else:
        ans.append(b - a % b)

    for i in ans:
        print(i)


