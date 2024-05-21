from collections import defaultdict
from heapq import heapify,heappop,heappush
n = int(input())
bab = list(map(int,input().split()))
graph = {i:i for i in range(1,n+1)}
size = [1]*(n+1)
def find(x):
    if x == graph[x]:
        return x
    graph[x] = find(graph[x])
    return graph[x]

def union(x,y):
    xp = find(x)
    yp = find(y)
    if xp != yp:
        
        if size[xp] >= size[yp]:
            graph[yp] = xp
            size[xp] += size[yp]
        else:
            graph[xp] = yp
            size[yp] += size[xp]
    else:
        return
for i in range(1,n+1):
    union(i,bab[i-1])
ans = set()
for i in range(1,n+1):
    if find(i) == find(bab[i-1]):
        ans.add(find(i))
# print(graph)
print(len(ans))
             
    