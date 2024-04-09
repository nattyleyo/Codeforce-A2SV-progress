tcase = int(input())
ls = list(map(int, input().split()))
left = 0
right = 0

for i in ls:
    if i > 0:
        left += i
    else:
        right += i

# print("left", left)
# print("right", right)
print(left - right)
