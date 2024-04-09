t = int(input())

for _ in range(t):
    n = int(input())

    sum_ = set()
    isSq = False
    arr = [0]*n
    for i in range(n):
        arr[i] = list(map(int, input()))
        sum_int = sum(arr[i])
        if sum_int != 0 and sum_int in sum_:
            isSq = True
        sum_.add(sum(arr[i]))
    if isSq:
        print("SQUARE")
    else:
        print("TRIANGLE")
