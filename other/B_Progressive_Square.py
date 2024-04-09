from collections import defaultdict,Counter
test = int(input())
def inbound(x,y):
    return (0 <= x < n) and (0 <= y < n)
for i in range(test):
    n,c,d = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    nums = Counter(nums)
    dic = defaultdict(int)
    grid = [ [0]*n for i in range(n)]
    # print(grid)
    grid[0][0] = min(nums)
    for i in range(n):
        for j in range(n):
            if inbound(i+1,j) and grid[i+1][j] == 0:
                grid[i+1][j] = grid[i][j] + c
            if inbound(i,j+1) and grid[i][j+1] == 0:
                grid[i][j+1] = grid[i][j] + d
    for i in range(n):
        for j in range(n):
            key = grid[i][j]
            dic[key] += 1
    if dic == nums:
        print('YES')
    else:
        print('NO')
                
            