t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = input()
    b = input()
    k = 0 
    j = 0 
    for i in range(n):
        while j < m and b[j] != a[i]:
            j += 1

        if j < m:
            k += 1
            j += 1
    print(k)