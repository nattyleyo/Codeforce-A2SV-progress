from collections import defaultdict
from heapq import heapify,heappop,heappush
test = int(input())
for c in range(test):
    n = int(input())
    soc = list(map(int,input().split()))
    soc = [(-soc[i],i+1) for i in range(len(soc))]
    idx = []
    heapify(soc)
    k = 0
    flag = True
    while len(soc) >= 2:
        max1,i = heappop(soc)
        max2,j = heappop(soc)
        if max1 != 0 and max2 != 0:
            idx.append([j,i])
            heappush(soc,(max1+1,i))
            heappush(soc,(max2+1,j))
            k += 1
    print(k)
    for tp in idx:
        print(*tp)