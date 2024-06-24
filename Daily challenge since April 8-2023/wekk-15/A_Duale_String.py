t = int(input())
for _ in range(t):
    s = list(input())
    flag = True
    if len(s)%2 == 0:
        mid = len(s)//2
        if s[:mid] == s[mid:]:
            flag = True
        else:
            flag = False 
    else:
        flag = False 
    if flag:
        print('YES')
    else:
        print('NO')