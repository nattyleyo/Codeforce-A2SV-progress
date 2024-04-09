n = int(input())
time = sorted(map(int, input().split()))
ans = waitTime = 0
for i in range(n):
    if waitTime <= time[i]:
        ans += 1
        waitTime += time[i]
print(ans)
