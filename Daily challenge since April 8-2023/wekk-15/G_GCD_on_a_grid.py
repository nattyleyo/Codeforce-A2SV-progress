test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    visited = set()
    vect = [(1, 0), (0, 1)]

    def inbound(x, y):
        return 0 <= x < n and 0 <= y < m

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def dfs(cell):
        x, y = cell

        if (x, y) == (n - 1, m - 1):
            return grid[x][y]

        maxi = 0
        for d in vect:
            i = x + d[0]
            j = y + d[1]
            if inbound(i, j):
                maxi = max(maxi, gcd(grid[x][y], dfs((i, j))))
            # print(maxi)
        return maxi

    print(dfs((0,0)))
