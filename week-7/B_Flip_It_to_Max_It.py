test = int(input())
for _ in range(test):
    n = int(input())
    my_list = list(map(int, input().split()))
    maxi_sum = sum(abs(a) for a in my_list)
    mini_op = 0
    left = 0
    right = 0
    flag = False
    while right < n:
        if my_list[right] < 0 and not flag:
            mini_op += 1
            flag = True
        if my_list[right] > 0:
            left = right+1
            flag = False
        right += 1
    print(maxi_sum, mini_op)
