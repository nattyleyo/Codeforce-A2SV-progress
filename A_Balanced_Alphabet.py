t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    x = ''.join(chr(97 + i) for i in range(k))
    rep = n // k
    rem = n % k
    s = x * rep + x[:rem]
    print(s)