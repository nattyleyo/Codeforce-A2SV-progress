test = int(input())
for i in range(test):
    col = int(input())
    row1 = input()
    row2 = input()
    left = 0
    flag = False
    while left < len(row1):
        if (row1[left] == row2[left]) or (row1[left] == 'G' and row2[left] == 'B') or (row1[left] == 'B' and row2[left] == 'G'):
            flag = True
        else:
            flag = False
            break
        left += 1
    if flag:
        print("YES")
    else:
        print('NO')
