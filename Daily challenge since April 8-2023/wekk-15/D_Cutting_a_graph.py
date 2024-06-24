from collections import defaultdict
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
            size[xp] += size[yp]
            
        else:
            graph[xp] = yp
            size[yp] += size[xp]
            

n,m,k = list(map(int,input().split()))
graph = {i:i for i in range(1,n+1)}
size = [1]*(n+1)     
for i in range(m):
    x,y = list(map(int,input().split()))
query = []
for i in range(k):
    cmd,u,v = list(input().split())
    query.append((cmd,int(u),int(v)))
n = len(query)
res = []
for i in range(-1,-n-1,-1):
    cmd,u,v = query[i]
    if cmd == 'ask':
        if find(u) == find(v):
            res.append('YES')
        else:
            res.append('NO')
    else:
        union(u,v)
m = len(res)    
for i in range(-1,-m-1,-1):
    print(res[i])
        
    

    
    
        
        