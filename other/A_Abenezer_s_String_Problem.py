from collections import defaultdict
test = int(input())
for _ in range(test):
    n = int(input())
    s = input()
    max_ord = 0
    for i in range(n):
        max_ord = max(max_ord, ord(s[i])-96)
    print(max_ord)
# down
# ^
# 4 15 23 13

# =
