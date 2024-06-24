t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    
    opt=1
    for i in range(n):
        opt += abs(a[i]-b[i])
        
    d = float('inf')
    
    for i in range(n):
        d = min(d,abs(a[i]-b[-1]),abs(b[i]-b[-1]))
        
    for i in range(n):
        if a[i]<=b[-1]<= b[i] or b[i]<=b[-1]<=a[i]:
            d = 0
            break
    opt += d
    print(opt)