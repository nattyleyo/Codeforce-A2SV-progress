test = int(input())
for _ in range(test):
    n = int(input())
    grid = [[0]*n for i in range(n)]
    grid[0] = list(map(int,input()))
    grid[n-1] = list(map(int,input()))
    # print(grid)
    vect = [(-1,-1),(-1,1)]
    visited = set()
    def inbound(x,y):
        return (0 <= x <n) and (0 <= y <n)
    def dfs(cell):
        x,y = cell
        visited.add(cell)
        c = 0
        
        for d in vect:
            i = x + d[0]
            j = y + d[1]
            if inbound(i,j) and (i,j) not in visited:
                dfs((x-1,y))
            