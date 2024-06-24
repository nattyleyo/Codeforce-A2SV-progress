test = int(input())
for _ in range(test):
    n = int(input())
    s = list('BAN'*n)
    # print(s)
    l = 0
    r = 3*n-1
    ans = []
    while l < r:
        if s[l] == 'B' and s[r] == 'N':
            s[l],s[r] = s[r],s[l]
            ans.append([l+1,r+1])
        l += 1
        r -= 1
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])
    