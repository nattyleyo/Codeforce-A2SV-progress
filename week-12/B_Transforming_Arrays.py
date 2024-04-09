t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    temp = 0
    flag = True
    for i in range(1, n):
        temp = b[i] - a[i]
        if a[i-1]*temp == 0:
            flag = False
            break
        if a[i] > b[i] or temp % a[i-1] != 0:
            flag = False
            break
        print(i)
    if flag:
        print("YES")
    else:
        print("NO")
