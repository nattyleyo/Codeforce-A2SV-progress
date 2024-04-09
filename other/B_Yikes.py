from bisect import bisect_left
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
res = [1]
pref = 0
for i in range(n):
    pref += nums[i]
    res.append(pref)
    if i!=n-1:
        res.append(pref+1)
# print(res)
pos =0
for i in range(m):
    pos = bisect_left(res,list2[i])
    # print(pos)
    pos //=2
    print(pos + 1)
    

    