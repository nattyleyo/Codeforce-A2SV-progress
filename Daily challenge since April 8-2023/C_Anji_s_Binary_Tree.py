from collections import defaultdict

test = int(input())
for _ in range(test):
    n = int(input())
    flag = input()
    graph = defaultdict(list)
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        l, r = 1, 1
        if flag[i - 1] == 'L':
            l = 0
        elif flag[i - 1] == 'R':
            r = 0
        graph[i].append((a, l))
        graph[i].append((b, r))
    
    stack = [(1,0)]
    ans = float('inf')
    edge = 0
    
    while stack:
        val,edge = stack.pop()
        child1 = graph[val][0]
        child2 = graph[val][1]
        
        
        if child1[0]==0 and child2[0]==0:
            ans = min(ans, edge)
            continue
        
        if child1[0]:
            x = edge + child1[1]
            stack.append((child1[0], x))
        if child2[0]:
            y = edge + child2[1]
            stack.append((child2[0], y))
    print(ans)
    
    #recursive way TLE on Test-3
    # def dfs(node):
    #     global ans
    #     val, edge = node
    #     child1 = graph[val][0]
    #     child2 = graph[val][1]
        
    #     visited.add(val)
        
    #     if child1[0]==0 and child2[0]==0:
    #         # print(node)
    #         ans = min(ans, edge)
    #         return
        
    #     if child1[0] and child1[0] not in visited:
    #         x = edge + child1[1]
    #         dfs((child1[0], x))
    #     if child2[0] and child2[0] not in visited:
    #         y = edge + child2[1]
    #         dfs((child2[0],y))
    
    # dfs((1, 0))
    # print(ans)
