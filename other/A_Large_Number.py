test = int(input())
for _ in range(test):
    n, d = list(map(int, input().split()))
    nums = input()
    res = ''
    for i in range(n):
        
        if int(nums[i]) < d:
            res = nums[:i] + str(d) + nums[i:]
            break
    if len(res) == 0:
        res = nums + str(d)
    print(res)
    