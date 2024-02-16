test = int(input())
for i in range(test):
    temp = list(map(int, input().split()))
    n = temp[0]
    m = temp[1]
    my_list = list(map(int, input().split()))
    space = 0
    my_list.sort(reverse=True)
    for i in range(n-1):
        space += my_list[i]
    space += my_list[0]+n
    if space <= m:
        print('YES')
    else:
        print("NO")
