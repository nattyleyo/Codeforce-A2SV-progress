n,m = list(map(int,input().split()))
sales = list(map(int,input().split()))
# print(sales)
ans = []
sales.sort()
for num in sales:
    if num < 0 and m > 0:
        ans.append(num)
        m -= 1

print(-sum(ans))