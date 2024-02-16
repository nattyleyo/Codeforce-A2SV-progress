from collections import defaultdict
n, k = list(map(int, input().split()))
s = input()
left = 0
right = 1
dic = {}
a_count = s.count('a')
b_count = s.count('b')
total_b = 0
max_str = n
max_str = 0
# 01234567
# abba
# ^
#   ^
dic[s[left]] = right
while right < n:
    # if s[left] == 'a':
    dic[s[right]] = right
    if s.count(s[left]) >= max(s.count('a'), s.count('b')) and total_b<=k:
        total_b += 1
        max_str += 1
    else:
        left = dic[s[right]]+1
        total_b -= 1
    max_str = max(max_str, dic['a']+1)
    right += 1
print(max_str)
