from collections import defaultdict, deque
from heapq import he
def solve():
    n = int(input())
    a = list(map(int,input().split()))
    si = input()
    graph = defaultdict(list)
     
    for i in range(2,n+1):
        color = si[i-1]
        graph[a[i-2]].append((i,color))
        graph[i].append((a[i-2],color))
    # print(graph)
    
    visited = set()
    ans = 0
    def dfs(node):
        nonlocal ans
        w,b = 0,0

        visited.add(node)

        if si[node-1] == "W":
            w += 1
        elif si[node-1] == "B":
            b += 1
        
        for d in graph[node]:
            if d[0] not in visited:
                x,y = dfs(d[0])
                b += x
                w += y
        if b == w:
            ans += 1

        return (b,w)
    
    dfs(1)
    print(ans)
    
    
def main():
    test = int(input())
    for _ in range(test):
        solve()

import sys, threading
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()