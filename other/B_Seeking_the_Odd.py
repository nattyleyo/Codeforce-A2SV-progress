test = int(input())
for _ in range(test):
    n = int(input())
    flag = False
    
  
    while n%2 == 0:
        n //=2
    if n%2 != 0 and n > 1:
        print('YES')
    else:
        print('NO')