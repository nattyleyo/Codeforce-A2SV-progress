n = int(input())
mat = []
good = 0
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
middle = (n-1)//2
for i in range(n):
    good += mat[i][i]
    good += mat[i][n-1-i]
    good += mat[middle][i]
    good += mat[i][middle]
good -= 3*mat[middle][middle]
print(good)


# o(n^2) complexity below
# for i in range(n):
#     for j in range(n):
#         if i-j == 0 or i+j == n-1 or i == middle or j == middle:
#             good += mat[i][j]
