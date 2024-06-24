from itertools import accumulate
n,k= list(map(int, input().split()))
pref = list(accumulate([5*i for i in range(1,n+1)]))
# print(pref)
contest = 4*60
low = 0
high = n-1

while low <= high:
    mid = (low+high)//2
    # print(mid)
    if k + pref[mid] <= contest:
        low = mid + 1
    else:
        high = mid - 1
print(low)