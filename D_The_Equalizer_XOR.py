test = int(input())
for _ in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    xor = 0
    for i in a:
        xor ^= i
    if xor==0 and xor in a:
        print('YES')
    else:
        print('NO')
    
    
    
    