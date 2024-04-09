test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    s = input()
    w = input()
    if m > n:
        print('NO')
        continue
    
    target = sum(ord(ch) for ch in w)
    strSum = sum(ord(ch) for ch in s[:m])
    flag = False
    for i in range(n-m+1):
        if strSum == target:
            flag = True
            break
        if i < n-m:
            strSum -= ord(s[i])
            strSum += ord(s[i+m])
                
    if flag:
        print('YES')
    else:
        print('NO')
