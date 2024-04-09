friends = list(map(int, input().split()))
maxi = max(friends)
mini = min(friends)
res = maxi - mini
print(res)
