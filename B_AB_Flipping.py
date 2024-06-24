test = int(input())
for _ in range(test):
    n = int(input())
    s = list(input())
    ans = 0
    swapped = {i:False for i in range(n)}
    for i in range(n-1):
        if s[i] == 'A' and s[i+1] == 'B':
            s[i],s[i+1] = s[i+1],s[i]
            swapped[i] = True
            ans += 1
    # print(swapped,s)
    if not swapped[0] and s[0] == 'A' and s[1] == 'B':
        ans += 1
    print(ans)
        
            
    
    
    