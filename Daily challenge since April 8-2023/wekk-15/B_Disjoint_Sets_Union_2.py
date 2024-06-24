from collections import defaultdict
from heapq import heapify,heappop,heappush
n,m = list(map(int,input().split()))
graph = {i:i for i in range(1,n+1)}
mini = {i:i for i in range(1,n+1)}
maxi = {i:i for i in range(1,n+1)}
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
            
            mini[xp] = min(mini[xp],mini[yp])
            maxi[xp] = max(maxi[xp],maxi[yp])
        else:
            graph[xp] = yp
            size[yp] += size[xp]
            
            mini[yp] = min(mini[xp],mini[yp])
            maxi[yp] = max(maxi[xp],maxi[yp])
            
for _ in range(m):
    q = list(input().split())
    u,v,x = -1,-1,-1
    if len(q) == 3:
        u,v = int(q[1]), int(q[2])
        union(u,v)
    else:
        x = int(q[1])
        xp = find(x)
        print(mini[xp],maxi[xp],size[xp])
    
        
        