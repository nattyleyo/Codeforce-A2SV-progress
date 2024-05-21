from collections import defaultdict,deque

graph = defaultdict(list)
n = int(input())
edge = list(map(int,input().split()))
color = list(map(int,input().split()))

for i in range(2,n+1):
    graph[i].append(edge[i-2])
    graph[edge[i-2]].append(i)
# print(graph)
que =deque([(1,color[0])])
visited =set()
li = [0]*n
ans = 0
if color[0] != 0:
    ans += 1
    li = [color[0]]*n
while que:
    node = que.popleft()
    visited.add(node[0])
    
    for d in graph[node[0]]:
        if d not in visited:
            if color[d-1] != node[1]:
                ans += 1
            li[d-1] = color[d-1]
            que.append((d,color[d-1]))
print(ans)
    

