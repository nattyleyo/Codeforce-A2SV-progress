from collections import defaultdict
def findDiv(number):
    fact = set([1,number])
    n = number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            fact.add(i)
            if i != number // i:
                fact.add(number // i)
    return fact

def solve(a, div):
    a.sort()
    print(a)
    count = [0] * (len(div)+1)
    tmp = [0] * (len(div)+1)
    
    ans = 0
    rem = n
    
    for e in a:
        rem -= 1
        val = 0

        for d in div[e]:
            val = count[d] - tmp[d]

            for d2 in div[d]:
                tmp[d2] += val

            ans += d * val * rem




    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    M = max(a)
    div = defaultdict(list)
    for i in range(1, M+1):
        x = list(findDiv(i))
        div[i].extend(x)
    # print(div) 
    
    
    ans = solve(a,div)
    print(ans)

