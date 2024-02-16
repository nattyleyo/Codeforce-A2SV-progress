test = int(input())
for i in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    my_set = set(arr)
    if len(my_set) != len(arr):
        print("NO")
    else:
        print('YES')
