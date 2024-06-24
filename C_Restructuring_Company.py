from collections import defaultdict

def find(x):
    if x == graph[x]:
        return x
    graph[x] = find(graph[x])
    return graph[x]

def union(x, y):
    xp = find(x) 
    yp = find(y)
    if xp != yp:
        if size[xp] >= size[yp]:
            graph[yp] = xp
            size[xp] += size[yp]
        else:
            graph[xp] = yp
            size[yp] += size[xp]

n, q = map(int, input().split())
graph = {i: i for i in range(1, n + 1)}
size = [1] * (n + 1)

for _ in range(q):
    tp, x, y = map(int, input().split())
    if tp == 1:
        union(x, y)
    elif tp == 2:
        x = min(graph.keys())
        while x < y:
            union(x, x + 1)
            x += 1
    else:
        if find(x) == find(y):
            print('YES')
        else:
            print('NO')