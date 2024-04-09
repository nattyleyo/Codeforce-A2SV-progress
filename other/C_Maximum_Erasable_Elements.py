from cmath import inf
import sys
num = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
_max, i = -inf, 1
while i-1 < len(nums) and nums[i-1] == i:
    i += 1
_max = i-2


partial, i = 0, 0
for i in range(len(nums)-1):
    partial += 1
    if nums[i] != nums[i+1] - 1:
        _max = max(_max, partial - 2)
        partial = 0
times = 0
for i in range(len(nums)-1, -1, -1):
    if nums[i] != 1000-times:
        break
    times += 1
_max = max(times-1, _max, partial - 1)
print(_max if _max > 0 else 0)
