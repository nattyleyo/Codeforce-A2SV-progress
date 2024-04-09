
from collections import defaultdict

test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int,input().split()))
    maxi = max(nums)
    
    fact = defaultdict(int)
    for i in range(n):
        d = 2
        while d*d <= nums[i]:
            while nums[i]%d == 0:
                fact[d] += 1
                nums[i] //= d
            d += 1
        if nums[i] > 1:
            fact[nums[i]] += 1
    # print(fact)
    flag = True
    for key in fact:
        if fact[key]%n != 0:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')
    