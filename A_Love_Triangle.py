from collections import defaultdict,deque
n = int(input())
f = list(map(int,input().split()))
graph = defaultdict(list)
for i in range(n):
    graph[i+1].append(f[i])

def bfs(node):
    que = deque([node])
    visited = set()  
    count = 0
    while que:
        x = que.popleft()
        visited.add(x)
        if count > 2:
            continue
        
        for d in graph[x]:
            if count == 2 and d == node:
                return True
            
            if d not in visited:
                que.append(d)
                count += 1
    
    return False

ans = False   
for i in range(n):
    ans = ans or bfs(i+1)

if ans:
    print('YES')
else:
    print('NO')