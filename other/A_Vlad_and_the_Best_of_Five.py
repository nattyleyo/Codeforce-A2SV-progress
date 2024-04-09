test = int(input())
for _ in range(test):
    n = 5
    s = input()
    count_a = s.count('A')
    count_b = s.count('B')
    if count_a >= count_b:
        print('A')
    else:
        print('B')
