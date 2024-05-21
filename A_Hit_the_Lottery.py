n = int(input())
bill = [100,20,10,5,1]
ans = 0
for i in range(len(bill)):
    while n >= bill[i]:
        ans += n//bill[i]
        n %= bill[i]
        # print(n,bill[i])
print(ans)