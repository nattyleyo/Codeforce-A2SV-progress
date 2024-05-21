from collections import defaultdict, deque
import heapq
n, m = list(map(int, input().split()))
graph = defaultdict(list)
indeg = [0] * (n+1)

for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    indeg[b] += 1

queue = []
order = []

for i in range(1, n+1):
    if indeg[i] == 0:
        heapq.heappush(queue,i)
while queue:
    node = heapq.heappop(queue)
    order.append(node)

    for d in graph[node]:
        indeg[d] -= 1
        
        if indeg[d] == 0:
            heapq.heappush(queue,d)

if len(order) != n:
    print(-1)
else:
    print(*order)
