def find(n, s):
    if s == 0:
        if n == 1:
            return "0 0"
        else:
            return "-1 -1"
    
    if s > 9 * n:
        return "-1 -1"
    
    mini = [0] * n
    Sum = s
    
    for i in range(n-1, -1, -1):
        if Sum > 9:
            mini[i] = 9
            Sum -= 9
        else:
            mini[i] = Sum
            Sum = 0
    
    if mini[0] == 0:
        for i in range(1, n):
            if mini[i] > 0:
                mini[i] -= 1
                mini[0] = 1
                break
    
    maxi = [0] * n
    Sum = s
    
    for i in range(n):
        if Sum > 9:
            maxi[i] = 9
            Sum -= 9
        else:
            maxi[i] = Sum
            Sum = 0
    
    return ''.join(map(str, mini)) + " " + ''.join(map(str, maxi))

n, s = map(int, input().split())
print(find(n, s))
