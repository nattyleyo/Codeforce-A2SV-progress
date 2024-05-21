class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {i:i for i in range(1,n+1)}
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

                else:
                    graph[xp] = yp
                    size[yp] += size[xp]
            else:
                return

        mini = float('inf')
        for u,v,d in roads:
            union(u,v)

        # print(graph)
        for u,v,d in roads:
            if find(1) == find(u) == find(v):
                mini = min(mini,d)
        return mini



# stack size
import sys, threading


def main():
    # your code
    
if name == 'main':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()