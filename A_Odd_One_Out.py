n = int(input())
for  i in range(n):
    a,b,c = list(map(int,input().split()))
    print(a^b^c)