test = int(input())
for _ in range(test):
    s = input()
    left = 0
    right = len(s)-1
    ans = 0
    my_set = set(s)
    flag = True
    if len(my_set)== 1:
        flag = False
    while flag and left < right:
        if s[left]==s[right]:
            ans = left + right
            left += 1
            right -= 1
        else:
            break 
    if flag:
        print(ans)
    else:
        print(-1)