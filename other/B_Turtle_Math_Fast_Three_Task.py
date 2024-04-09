test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    total = sum(nums)
    if total % 3 == 0:
        print(0)
    else:
        i = 0
        move = 0
        while i < len(nums):
            if nums[i] % 3 != 0:
                move = max(move, nums[i] % 3)
            i += 1
        print(move)
