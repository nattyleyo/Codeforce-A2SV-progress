t = int(input())

for _ in range(t):
    k = int(input())

    i = 1
    count = 0

    while count < k:
        if i % 3 != 0 and i % 10 != 3:
            count += 1
        if count < k:
            i += 1

    print(i)
