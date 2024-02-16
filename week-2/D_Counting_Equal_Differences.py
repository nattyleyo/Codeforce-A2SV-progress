t = int(input())
for _ in range(t):
    m = int(input())
    nums = list(map(int, input().split()))
    count = 0
    difference_count = {}
    for j in range(m):
        diff = nums[j] - j
        if diff in difference_count:
            count += difference_count[diff]
        difference_count[diff] = difference_count.get(diff, 0) + 1
    print(count)
