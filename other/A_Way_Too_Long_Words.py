test = int(input())
for _ in range(test):
    s = input()
    n = len(s)
    if n <= 10:
        print(s)
    else:
        ans = s[0] + str(n-2) + s[-1]
        print(ans)