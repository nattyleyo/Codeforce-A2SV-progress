k,n,w = list(map(int,input().split()))
x = 0
for i in range(1,w+1):
    x += i*k
print(abs(n-x) if n < x else 0)
