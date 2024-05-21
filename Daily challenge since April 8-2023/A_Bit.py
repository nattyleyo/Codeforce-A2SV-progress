n = int(input())
ans = 0
for i in range(n):
    st = input()
    if st[0] == '+' or st[-1] == '+':
        ans += 1
    elif st[0] == '-' or st[-1] == '-':
        ans -= 1
print(ans)
    