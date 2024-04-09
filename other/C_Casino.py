n = int(input())
nums = list(map(int,input().split()))
ans =set()
for i in range(n):
    while nums[i]%2 == 0:
        nums[i] //=2
    while nums[i]%3 == 0:
        nums[i] //=3
    ans.add(nums[i])
if len(ans) == 1:
    print('Yes')
else:
    print('No')