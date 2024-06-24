test = int(input())
for _ in range(test):
    x = int(input())
    y = x&-x
    
    while x^y == 0 or x&y == 0:
        y += 1
    print(y)
    
        