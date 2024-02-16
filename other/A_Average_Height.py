t = int(input())
for x in range(t):
    m = int(input())
    num = list(map(int, input().split()))
    odd = []
    even = []
    for i in range(len(num)):
        if num[i] % 2 != 0:
            odd.append(num[i])
        else:
            even.append(num[i])
    for j in odd:
        print(j, end=' ')
    for j in even:
        print(j, end=' ')
    print('')
