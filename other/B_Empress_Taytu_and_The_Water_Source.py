from math import ceil
test = int(input())
for _ in range(test):
    n,k = list(map(int,input().split()))
    dem = list(map(int,input().split()))
    time = list(map(int,input().split()))
    flag = True
    ans = -1
    if sum(time) > k:
        flag = False
    def isTotal(mid):
        total = 0
        for i in range(len(dem)):
            temp = ceil(dem[i]/mid)
            total += temp*time[i]
        return total
    low = 1
    high = max(dem)
    while flag and  low <= high:
        mid =(low+high)//2
       
        if isTotal(mid) <= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
        
        
        
    