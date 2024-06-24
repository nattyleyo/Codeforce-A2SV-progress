n = int(input())
a = list(map(int,input().split()))
a = [(a[i],i+1) for i in range(n)]
a.sort()
l = 0
r = n-1
ans = []
while l < r:
    x = a[l][1]
    y = a[r][1]
    ans.append(str(x)+' '+str(y))
    l +=1
    r -=1
for i in range(n//2):
    print(ans[i])