from collections import defaultdict
n,m = list(map(int,input().split()))
graph = defaultdict(list)
for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

ans = 0
visited =set()

def dfs(node):
    flag = True
    stack = [node]
    visited.add(node)
    
    while stack:
        node = stack.pop()
    
        if len(graph[node])!=2:
            flag = False
        
        for d in graph[node]:

            if d not in visited:
                visited.add(d)  
                stack.append(d)
    return flag
        
    

for key in graph:
    if key not in visited:
        if dfs(key):
            ans += 1
print(ans)
    