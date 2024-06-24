test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    for i in range(n-1):
        if abs(nums[i]-nums[i+1]) > 1:
            print('NO')
            break
    else:
        print('YES')
    