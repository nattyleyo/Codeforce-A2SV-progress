from collections import Counter
from heapq import heapify,heappop,heappush
from itertools import accumulate
n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
pref = list(accumulate(a))
heap = a[:n-1]
print(pref)
heapify(heap)
x = 0
i = k-1
while i > 0:
    x += heappop(heap)
    i -= 1
print(k*pref[n-1] - x)
    
    

