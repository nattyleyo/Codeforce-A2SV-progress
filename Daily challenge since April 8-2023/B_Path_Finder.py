from collections import defaultdict,deque

n = int(input())
graph = defaultdict(list)
for i in range(n-1):
    a,b,w = list(map(int,input().split()))
    graph[a].append((b,w))
    graph[b].append((a,w))
maxi = 0
stack = [(0,0)]
visited = set()
while stack:
    node = stack.pop()
    visited.add(node[0])
    for d in graph[node[0]]:
        if d[0] not in visited:
            total = node[1]+d[1]
            stack.append((d[0],total))
            maxi = max(maxi,total)
print(maxi)

