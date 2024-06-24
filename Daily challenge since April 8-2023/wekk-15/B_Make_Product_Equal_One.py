n = int(input())
a = list(map(int,input().split()))

def dp(i):
    if i >= n:
        return 0
    
    if prd == 1:
        return
    add = a[i]+1+dp(i+1)
    sub = a[i]-1+dp(i+1)
