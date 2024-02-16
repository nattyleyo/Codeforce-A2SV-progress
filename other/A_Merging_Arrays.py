n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
left = 0
right = 0
res = []
while left < n and right < m:
    if arr1[left] < arr2[right]:
        res.append(arr1[left])
        left += 1
    else:
        res.append(arr2[right])
        right += 1
res.extend(arr1[left:])
res.extend(arr2[right:])
print(' '.join([str(num) for num in res]))
