days = int(input())
meats = []
for i in range(days):
    need, price = map(int, input().split())
    meats.append((need, price))
flag = True
total = 0
mini = float('inf')
l = 0
r = 1
# total += meats[0][0]*meats[0][1]
for i in range(len(meats)):
    mini = min(mini, meats[i][1])
    total += (meats[i][0]*mini)
print(total)
