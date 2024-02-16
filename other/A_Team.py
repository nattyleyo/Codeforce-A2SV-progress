matrix = []
n = int(input())
total = 0
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(n):
    count = 0
    for j in range(3):
        if matrix[i][j] == 1:
            count = count + 1
    if (count >= 2):
        total = total + 1
print(total)
