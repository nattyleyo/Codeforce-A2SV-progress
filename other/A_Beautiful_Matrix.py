matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
move = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            move = abs(j - 2) + abs(i - 2)
            break
print(move)
