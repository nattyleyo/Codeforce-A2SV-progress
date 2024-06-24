from collections import defaultdict,Counter
from heapq import heapify,heappop,heappush
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
            comp[xp-1].extend(comp[yp-1])
            size[xp] += size[yp]
        else:
            graph[xp] = yp
            comp[yp-1].extend(comp[xp-1])
            size[yp] += size[xp]
    else:
        return
                
    
n = int(input())
graph = {i:i for i in range(1,(2*n)+1)}
size = [1]*(n+1)
comp = [[i] for i in range(1,n+1)]
for i in range(n-1):
    u,v = list(map(int,input().split()))
    union(u,v)
x = find(1)
print(*comp[x-1])

             
    