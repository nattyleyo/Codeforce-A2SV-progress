from collections import defaultdict,deque

n = int(input())
nums = list(map(int,input().split()))
di  = {'chest':0,'biceps':1,'back':2}
count  = defaultdict(int)
for key in di:
    val = di[key]
    i = val
    while i < n :
        count[key] += nums[i]
        i += 3
        # print(key,count[key])
maxi = max(count.values())
for key in di:
    if count[key]==maxi:
        print(key)
        break

