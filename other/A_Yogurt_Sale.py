test = int(input())
for i in range(test):
    n,a,b = list(map(int,input().split()))
    ans = 0
    q = n//2
    r = n%2
    
    if n % 2 == 0:
        ans = min(n*a,q*b)
        
    elif 2*a < b:
        ans = n * a
    else:
        ans = q*b + r*a
        
    print(ans)