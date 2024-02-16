test = int(input())
for i in range(test):
    size = list(map(int, input().split()))
    n = size[0]
    m = size[1]
    mat = []
    maxSum = 0
    forward_dict = defaultdict(int)
    backward_dict = defaultdict(int)
    for _ in range(n):
        row = list(map(int, input().split()))
        mat.append(row)
    for i in range(n):
        for j in range(m):
            forward_dict[i-j] += mat[i][j]
            backward_dict[i+j] += mat[i][j]
    for i in range(n):
        for j in range(m):
            tempSum = forward_dict[i-j]+backward_dict[i+j]-mat[i][j]
            maxSum = max(maxSum, tempSum)
    print(maxSum)
