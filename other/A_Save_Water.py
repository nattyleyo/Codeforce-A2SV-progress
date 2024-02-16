n = int(input())
m = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

count = 0
arr.sort(reverse=True)

sum_ = 0

for i in range(n):
    sum_ += arr[i]
    count += 1
    if sum_ >= m:
        break

print(count)
