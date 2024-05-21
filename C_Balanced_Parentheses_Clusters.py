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
            size[xp] += size[yp]
        else:
            graph[xp] = yp
            size[yp] += size[xp]
    else:
        return
def isBalanced(l,r,s):
    br = Counter(s[l:r+1])
    if br['('] == br[')']:
        return True
    return False
    
        
                
    
test = int(input())
flag = True
for _ in range(test):
    n = int(input())
    s = list(input())
    stack = []
    graph = {i:i for i in range(1,(2*n)+1)}
    # print(graph)
    size = [1]*(2*n+1)
    # union(1,2*n)
    for i in range(2*n):
        if stack and s[i] == ')':
            x,k = stack.pop()
            union(k+1,i+1)
            if i+1 < 2*n and s[i+1] == '(':
                union(k+1,i+2)
        elif s[i] == '(':
            stack.append((s[i],i))
            # print(s,stack)
        
    # print(graph)
    ans = set()
    for key in graph:
        x = find(graph[key]) 
        ans.add(x)  
    print(len(ans))
             
    