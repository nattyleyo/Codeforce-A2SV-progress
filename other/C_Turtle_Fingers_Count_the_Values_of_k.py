test = int(input())
for _ in range(test):
    nums = list(map(int, input().split()))
    a, b, l = nums[0], nums[1], nums[2]
    mini = min(nums)
    maxi = max(nums)
    count = 1
    total1 = l
    while total1 % mini == 0:
        total1 /= mini
        count += 2
    total2 = l
    while total2 % mini == 0:
        total2 /= maxi
        count += 1
    print(count)
