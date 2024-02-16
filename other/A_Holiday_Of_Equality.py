n = int(input())
str = input()
dif = [0]*n
res = 0
num = list(map(int, str.split()))
for i in range(n):
    newNum = sorted(num)
    dif[i] = newNum[n-1]-newNum[i]
for i in range(n):
    res += dif[i]
print(res)
