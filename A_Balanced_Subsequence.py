from collections import Counter
n,k = map(int, input().split())
s = input()
# ACAABCCAB
#         ^
count = Counter(s)
mini = min(count.values())
count = {i:mini for i in count}
# print(count,mini)
ans = 0
if len(count) == k:
    for i in range(n):
        if count[s[i]] > 0:
            count[s[i]] -= 1
            ans += 1
    print(ans)   
else:
    print(ans)
