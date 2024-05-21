# from math import ceil
n,k = list(map(int,input().split()))
nums = list(map(int,input().split()))
# print(nums)
ans = 0
for i in range(n):
    if nums[i] > 0 and nums[i] >= nums[k-1]:
        ans += 1
print(ans)