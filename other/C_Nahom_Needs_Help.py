n, m, k = map(int, input().split())
my_list = list(map(int, input().split()))
query = []
oper = []
for _ in range(m):
    row = list(map(int, input().split()))
    query.append(row)
for _ in range(k):
    row = list(map(int, input().split()))
    oper.append(row)
arr = [0]*(m+1)
for i in range(k):
    arr[oper[i][0]-1] += 1
    arr[oper[i][1]] -= 1

pref_1 = [0]*(m+1)
pref_1[0] = arr[0]

for i in range(1, m):
    pref_1[i] = pref_1[i-1] + arr[i]
for i in range(m):
    query[i][2] *= pref_1[i]

# print(query)
arr_2 = [0]*(len(my_list)+1)
for i in range(m):
    arr_2[query[i][0]-1] += query[i][2]
    arr_2[query[i][1]] -= query[i][2]
pref_2 = [0]*(len(my_list)+1)
pref_2[0] = arr_2[0]
for i in range(1, len(my_list)):
    pref_2[i] = pref_2[i-1] + arr_2[i]

for i in range(len(my_list)):
    my_list[i] += pref_2[i]

print(' '.join(str(s) for s in my_list))
# 1 2 3
# 1 0-1
# 1 0 0 -1
# 0 1   -1
# 2 1-1 -2
# 2 3 2 0

# 1 2 2
# 1 3 6
# 2 3 8
#
# 2 0 -2
# 6 0  0 -6
# 0 8  0 -8
# +
# 8 8 -2 -14
# 8 16 14 0
# 1 2  3
# =9 18 17
