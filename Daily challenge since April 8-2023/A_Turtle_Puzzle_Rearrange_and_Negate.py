test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        ans += abs(nums[i])
    print(ans)