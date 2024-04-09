from collections import defaultdict
from decimal import Decimal
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dic = defaultdict(int)
ans = 0
zero = 0 
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def fraction(b,a):
    print(b,a,gcd(a,b))
    return b//gcd(a,b) , a//gcd(a,b)

for i in range(n):
    if a[i] == 0 and b[i] == 0:
        zero += 1
    elif a[i] != 0:
        d = fraction(b[i],a[i])
        dic[d] += 1
ans += zero
if dic:
    ans += max(dic.values())
# print(ans)
# print(gcd(50,))
                   
       