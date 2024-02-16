t = int(input())
for i in range(t):
    oper = int(input())
    Str = input()
    p = 0
    q = 1
    count = 1
    while q < len(Str):
        if Str[p:q+1] not in Str[q+1:]:
            count += 1
        else:
            count += 1
            break
        q += 1
        p += 1
    if count < oper:
        print("YES")
    else:
        print("NO")
