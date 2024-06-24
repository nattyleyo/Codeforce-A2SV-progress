from math import gcd
test = int(input())
for _ in range(test):
    x = int(input())
    maxi = float('-inf')
    dic = {}
    for i in range(1,x):
        maxi = gcd(x,i)+i
        if maxi in dic:
            dic[maxi].append(i)
        else:
            dic[maxi] = [i]
        maxi = max(maxi,gcd(x,i)+i)
    # print(dic[maxi])
    print(min(dic[maxi]))
        