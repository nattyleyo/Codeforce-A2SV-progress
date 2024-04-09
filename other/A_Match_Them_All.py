from collections import defaultdict
test = int(input())
for _ in range(test):
    n = int(input())
    li = ['0']*n
    count = defaultdict(int)
    flag = True
    for i in range(n):
        li[i] = input()
    for i in range(len(li)):
        for j in range(len(li[i])):
            count[li[i][j]] += 1
    for key in count:
        if count[key] % n != 0:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
