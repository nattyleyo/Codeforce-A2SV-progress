from collections import defaultdict,deque
n,m = list(map(int,input().split()))
graph = defaultdict(list)
indeg = [0]*(n+1)
for i in range(1,n+m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    indeg[b] += 1
# print(graph)
que = deque()
ans = [0]*(n+1)
for i in range(1,len(indeg)):
    if indeg[i] == 0:
        que.append(i)
while que:
    node = que.popleft()
        
    for d in graph[node]:
        indeg[d] -= 1
        if indeg[d] == 0:
            ans[d] = node
            que.append(d)
for i in range(1,len(ans)):
    print(ans[i])
