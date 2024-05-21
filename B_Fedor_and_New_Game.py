n,m,k = list(map(int,input().split()))
player = []
for i in range(m+1):
    a = int(input())
    player.append(a)
fedor = player.pop()
# print(player)
count = 0
for p in player:
    res = p^fedor
    ones = 0
    for i in range(32):
        if res&(1<<i):
            ones += 1
    if ones <= k:
        count += 1
print(count)    
    
    # print(bin(a)[2:])
"""
6543210
0001000
0000101
1101111

0010001
210
001
010
011

100
111
"""