test = int(input())
for _ in range(test):
    n = int(input())
    li = list(map(int, input().split()))
    temp_li = sorted(li)
    ans = [0]*n
    first_max = temp_li[n-1]
    sec_max = temp_li[n-2]
    for i in range(n):
        if li[i] == first_max:
            ans[i] = li[i]-sec_max
        else:
            ans[i] = li[i]-first_max
    print(' '.join(map(str, ans)))
