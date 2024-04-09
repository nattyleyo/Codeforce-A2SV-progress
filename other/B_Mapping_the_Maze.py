from collections import defaultdict

n,m=list(map(int,input().split()))
graph = defaultdict(list)
# bus,ring,star = True,True,True
for i in range(m):
    a,b=list(map(int,input().split()))
    if i == 0:
        source = a
    graph[a].append(b)
print(graph) 
if len(graph)== 1:
    for key in graph:
        val = graph[key]
        if len(val) > 1:
            print("star topology")
            continue
visited = set()
ring = False
stack = [source]
un = True
while stack:
    node = stack.pop()   
    
    if node in visited and not ring:
        un = True
   
    visited.add(node)
    for d in graph[node]:
        if d not in visited:
            stack.append(d)
        else:
            ring = True
if len(visited)== n and not ring:
    print('bus topology')
elif not un and ring:
    print('ring topology') 
elif un :
    print('unknown topology') 
            
                




        
