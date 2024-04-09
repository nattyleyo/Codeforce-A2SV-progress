# from collections import defaultdict
# st = input()
# s = list(st)
# count = defaultdict(int)
# for i in range(len(s)):
#     count[s[i]] = i
# # print(count)
# left = 0
# right = 1
# res = []
# while right < len(s):
#     if s[left] == s[right]:
#         if right < count[s[right]]:
#             s[right] = s[count[s[right]]+1]
#         else:
#             s[left] = s[count[s[right]]+1]
#     # print(s)
#     left += 1
#     right += 1
# print(''.join(s))
ls = list(input())
s = []


def push(x):
    if len(s) == 0:
        s.append(x)
    elif s[-1] == x:
        s.append(4)
    else:
        s.append(x)


for i in ls:
    push(i)

for i in range(len(s)):
    if i == len(s) - 1 and s[i] == 4:
        s[i] = chr(ord(s[i-1]) + 1)

    elif s[i] == 4:
        if chr(ord(s[i-1]) + 1) != s[i+1]:
            s[i] = chr(((ord(s[i-1]) + 1) % 26) + 97)
            # print("yes")
        else:
            s[i] = chr(((ord(s[i-1])+2) % 26) + 97)

s = "".join(s)
print(s)
