test = int(input())
for i in range(test):
    temp = list(map(int, input().split()))
    n = temp[0]
    m = temp[1]
    mat = []
    my_set = set()
    for _ in range(n):
        row = list(map(int, input().split()))
        mat.append(row)
    for i in range(n):
        row = sorted(mat[i])
        for j in range(m):
            if row[j] != mat[i][j]:
                my_set.add(j)
    print(my_set)
    if len(my_set) == 2:
        my_list = list(my_set)
        print(my_list[0])
