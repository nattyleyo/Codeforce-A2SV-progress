test = int(input())

for _ in range(test):
    n = int(input())
    x = list(map(int, input().split()))

    a = [0] * n
    a[0] = x[0] + 1

    for i in range(n-1):
        diff = (x[i+1] - x[i]) // x[i]
        a[i] = a[i] + diff * x[i]
        if a[i+1] % x[i+1] != x[i]:
            a[i+1] += x[i]

    print(' '.join(map(str, a)))