n = int(input())
res = [0]*n
flag = True
for i in range(n):
    s = input()
    res[i]=s
res.sort(key=lambda x: len(x))
for i in range(n-1):
    if res[i] not in res[i+1]:
        flag=False
if flag:
    print("YES")
    for i in range(len(res)):
        print(res[i])
else:
    print("NO")
