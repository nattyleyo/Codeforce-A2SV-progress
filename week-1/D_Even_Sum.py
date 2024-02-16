t = int(input())
max = 0
odd = 0
even = 0
nums = [0]*t
nums = list(map(int, input().split()))
for i in nums:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
nums = sorted(nums, reverse=True)
if odd % 2 == 0:
    sum = 0
    for i in nums:
        sum += i
else:
    sum = 0
    for i in range(len(nums)-1):
        sum += nums[i]
max = sum
print(max)
