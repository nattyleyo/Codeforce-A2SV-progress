n,m=list(map(int,input().split()))
grid = []
for i in range(n):
    row = list(map(int,input()))
    grid.append(row)
# print(grid)
vect = [(0,-1),(0,1),(-1,0),(1,0)]
visited = set()
ans = True
def inbound(x,y):
    return (0 <= x < n) and (0 <= y < m)
def helper(x,y):
    global ans
    # x,y = cell
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

ans = True
stack = [(0,0)]
while stack:
    x,y = stack.pop()
    visited.add((x,y))
    ans = helper(x,y)
    if not ans:
        break
    for d in vect:
        i = x + d[0]
        j = y + d[1]
        if inbound(i,j) and (i,j) not in visited:
            stack.append((i,j))
    
    
if ans:
    print('YES')
else:
    print('NO')
    
