n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
p,q = a[0],b[0]
ans = set()
for i in range(1,p+1):  
    ans.add(a[i])
for i in range(1,q+1):  
    ans.add(b[i])
# print(ans)
if len(ans)==n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')