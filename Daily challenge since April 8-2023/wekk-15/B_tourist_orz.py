test = int(input())
for _ in range(test):
    n,z = list(map(int,input().split()))
    a = list(map(int,input().split()))
    maxi = float('-inf')
    for i in range(n):
        a[i] |= z
        z &= a[i]
        maxi = max(maxi,a[i])
    print(maxi) 
        
    