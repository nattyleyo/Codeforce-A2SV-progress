test = int(input())
for _ in range(test):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    flag = True
    for i in range(n):
        if arr[i+n]-arr[i] < x:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')
