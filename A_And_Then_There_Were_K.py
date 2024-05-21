
test = int(input())
for _ in range(test):
    n = int(input())
    m = 0
    for i in range(32):
        if (n>>i)&1 == 1:
            m = i
        
    k = (2**m)-1
    print(k)
'''

210
  101


'''