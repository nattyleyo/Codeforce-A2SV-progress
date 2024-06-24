n,h = list(map(int,input().split()))
nums = list(map(int,input().split()))
ans = n
for x in nums:
    ans += (x > h)
print(ans)