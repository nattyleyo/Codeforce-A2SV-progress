# from collections import defaultdict

# def find(x):
#     if x == graph[x]:
#         return x
#     graph[x] = find(graph[x])
#     return graph[x]

# def union(x,y):
#     xp = find(x) 
#     yp = find(y)
#     if xp != yp:
#         if size[xp] >= size[yp]:
#             graph[yp] = xp
#             size[xp] += size[yp]
            
#         else:
#             graph[xp] = yp
#             size[yp] += size[xp]
#     else:
#         return
            

# n,q = list(map(int,input().split()))
# graph = {i:i for i in range(1,n+1)}
# node = set(range(1,n+1))
# size = [1]*(n+1)

# for _ in range(q):
#     tp,x,y = list(map(int,input().split()))
#     if tp == 1:
#         union(x,y)
#     elif tp == 2:
#         while x<y:
#             x = min(node,key=lambda k: k >= x)
#             node.remove(x)
#             union(x,x+1)
#             x += 1
#     else:
#         if find(x) == find(y):
#             print('YES')
#         else:
#             print('NO')
            
from collections import defaultdict


class Company:
    def __init__(self, n):
        self.parent = [-1] * (n + 1)
        self.unconnected = set(range(n + 1))

    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_two(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return x
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return x

    def union_range(self, x, y):
        pos = x
        while pos < y:
            pos = min(self.unconnected, key=lambda k: k >= pos)
            self.unconnected.remove(pos)
            self.union_two(pos, pos + 1)
            pos += 1


n, q = map(int, input().split())
company = Company(n)
for _ in range(q):
    tp, x, y = map(int, input().split())
    if tp == 1:
        company.union_two(x, y)
    elif tp == 2:
        company.union_range(x, y)
    else:
        print("YES" if company.find(x) == company.find(y) else "NO")