n = int(input())
s = input()
vowel = set(['a','e','i','o','u','y'])
stack = []
for i in range(n):
    if stack and stack[-1] in vowel and s[i] in vowel:
        continue
    stack.append(s[i])