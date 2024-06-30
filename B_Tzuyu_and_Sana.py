from collections import Counter
t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    # 4^x + 9^x
    # 3210
    # 1001
    # 0100
    # 1101
    print(a^b)
