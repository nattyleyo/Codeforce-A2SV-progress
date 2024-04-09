stack = []
now = 1
ans = 0
for _ in range(2*int(input())):
    # print(stack)
    inp = list((input().split()))
    if len(inp) > 1:
        stack.append(int(inp[1]))
    else:
        if stack:
            if stack[-1] == now:
                stack.pop()
            else:
                stack.clear()
                ans += 1
        now += 1
print(ans)
