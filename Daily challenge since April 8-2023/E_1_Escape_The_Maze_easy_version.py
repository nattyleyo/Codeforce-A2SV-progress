from collections import defaultdict,deque
test = int(input())
for _ in range(test):
    space = input()
    n,k = list(map(int,input().split()))
    frd = list(map(int,input().split()))
    graph = defaultdict(list)
    for i in range(n-1):
        a,b = list(map(int,input().split()))
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    ans = set()
    visited = set()
    queue = deque([(i,'f') for i in frd ])
    queue.append((1,'v'))
    while queue:
        for i in range(len(queue)):
            node =  queue.popleft()
            visited.add(node[0])
            for d in graph[node[0]]:
                if d not in visited:
                    if len(graph[d])==1: 
                        ans.add(node[1])
                    else:
                        visited.add(d)    
                        queue.append((d,node[1]))
    if 'v' in ans:
        print("YES")
    else:
        print("NO")