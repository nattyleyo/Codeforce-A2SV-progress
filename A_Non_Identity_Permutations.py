test =int(input())
for _ in range(test):
    n =int(input())
    ans = []
    ans.append(n)
    for i in range(1,n):
        ans.append(i)
    print(*ans)
