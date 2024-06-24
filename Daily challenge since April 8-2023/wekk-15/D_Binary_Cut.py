from collections import defaultdict
test = int(input())
for _ in range(test):
    s = list(input())
    dic = {'01': 1}
    ans = []
    stack = []
    
    for i in range(len(s)):
        if stack and int(s[i]) < int(stack[-1]):
            ans.append(stack)
            stack = []
        stack.append(s[i])
    if stack:
        ans.append(stack)
    cnt = 0
    for i in range(len(ans)):
        x = ''.join(ans[i])
        if '01' in x and dic['01'] > 0:
            dic['01'] -= 1
            cnt += 1
        elif '01' in x and dic['01'] == 0:
            cnt += 2
        else:
            cnt += 1
    print(cnt)
        
            