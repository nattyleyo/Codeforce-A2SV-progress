import heapq

n, k, q = map(int, input().split())
friends = list(map(int, input().split()))

heap = []
for _ in range(q):
    ty, fid = map(int, input().split())
    
    if ty == 1:
        heapq.heappush(heap, friends[fid - 1])
        
        if len(heap) > k:
            heapq.heappop(heap)
    else:
        if friends[fid - 1] in heap:
            print("YES")
        else:
            print("NO")