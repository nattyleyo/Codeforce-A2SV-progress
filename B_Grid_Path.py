def inbound(x,y):
    return (0<=x<n) and (0<=y<m)

test = int(input())
for _ in range(test):
    n,m,k = list(map(int,input().split()))
    cost = n * m - 1
    if k == cost:
        print("YES")
    else:
        print("NO")
    