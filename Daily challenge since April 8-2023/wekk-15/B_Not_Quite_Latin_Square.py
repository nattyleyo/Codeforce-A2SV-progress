from collections import defaultdict
res = {1:'A',2:'B',3:'C'}
dic = {'A':1,'B':2,'C':3,'?':0}
test = int(input())
for _ in range(test):
    grid = []
    ans = 0
    for i in range(3):
        row = list(input())
        grid.append(row)
    for i in range(3):
        for j in range(3):
            c = grid[i][j]
            ans ^= dic[c]
    print(res[ans])
    # print(dic[ans])
        