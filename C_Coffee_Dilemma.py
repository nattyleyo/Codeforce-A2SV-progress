from heapq import heappop,heappush
n = int(input())
a = list(map(int, input().split()))
heap = []
h = 0
for val in a:
    h += val
    heappush(heap,val)
    while h < 0 and heap:
        h -= heappop(heap)
print(len(heap))
        