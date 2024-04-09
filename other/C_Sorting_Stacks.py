test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    cur = 0
    flag = True

    for i in range(n):
        cur += nums[i] - i
        if cur < 0:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
    # 0 1 2
    # 0 1 0
    #     ^
    # cur= 0
