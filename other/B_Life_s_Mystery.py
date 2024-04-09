s = input()
stack = []
right = 0
popped = False
while right < len(s):
    if stack and stack[-1] == s[right]:
        stack.pop()
        popped = True
        # right += 1
    if not popped:
        stack.append(s[right])
    popped = False
    right += 1
print(''.join(stack))
