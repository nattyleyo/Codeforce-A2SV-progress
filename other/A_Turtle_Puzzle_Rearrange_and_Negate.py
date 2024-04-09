test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    my_sum = 0
    for i in range(n):
        my_sum += abs(nums[i])
    print(my_sum)
