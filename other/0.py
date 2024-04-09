import threading, sys
n,m=list(map(int,input().split()))
grid = []
for i in range(n):
    row = list(map(int,input()))
    grid.append(row)
# print(grid)
vect = [(0,-1),(0,1),(-1,0),(1,0)]
visited = set()
def main():
   
    ans = True
    def inbound(x,y):
        return (0 <= x < n) and (0 <= y < m)
    def helper(cell):
        nonlocal ans
        x,y = cell
        count = 0
        for d in range(len(vect)):
            i = x + vect[d][0]
            j = y  + vect[d][1]
            if count < 2 and inbound(i,j) and grid[x][y] != grid[i][j]:
                ans = False
                break
            elif count >= 2 and inbound(i,j) and grid[x][y] == grid[i][j]:
                ans = False
                break
            count += 1
        return ans

    def dfs(cell):
        nonlocal ans
        if not ans:
            return
        x,y = cell
        visited.add(cell)
        
        ans = helper(cell)
        
        for d in vect:
            i = x + d[0]
            j = y + d[1]
            if inbound(i,j) and (i,j) not in visited and ans:
                dfs((i,j))
        # print(flag)
        
    dfs((0,0))
    return ans
ans = main()
if ans:
    print('YES')
else:
    print('NO')
    
threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_theread = threading.Thread(target=main)
main_theread.start()
main_theread.join()