from collections import defaultdict
test = int(input())
for i in range(test):
    n = int(input())
    my_list = list(map(int, input().split()))
    di = defaultdict(int)
    for i in range(len(my_list)):
        if my_list[i] in di:
            di[my_list[i]] = -1
        else:
            di[my_list[i]] = i
    for key, val in di.items():
        if di[key] != -1:
            print(val+1)
            break
