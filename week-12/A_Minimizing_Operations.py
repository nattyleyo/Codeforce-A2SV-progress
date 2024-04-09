test = int(input())
for _ in range(test):
    n = int(input())
    li = list(map(int, input().split()))
    min_val = min(li)
    max_val = max(li)
    print(max_val-min_val)
