test = int(input())
for _ in range(test):
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    res = 0
    for i in range(30,-1,-1):
        zero = 0
        for num in a:
            if num&(1<<i) == 0:
                zero += 1
        if zero <= k:
            res |= (1<<i)
            k -= zero
    print(res)
     
        
    