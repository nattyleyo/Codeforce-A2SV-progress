from collections import defaultdict
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    count = defaultdict(list)
    left = 0
    right = 0
    max_range = -1

    while right < n:
        temp = count[a[right]]
        if count[a[right]] in count:
            while count[a[left]][1] >= k:
                left = count[a[left]][0] + 1
            if count[a[left]][1] < k:
                left = temp[0]

        temp[0] = right
        temp[1] += 1
        right += 1
