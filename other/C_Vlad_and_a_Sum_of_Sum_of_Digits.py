from itertools import accumulate
arr = [sum(int(i) for i in list(str(num))) for num in range(2*pow(10, 5)+1)]
arr = list(accumulate(arr))

for _ in range(int(input())):
    print(arr[int(input())])
