first = list(map(int,input().split('+')))
first.sort()
print('+'.join([str(i) for i in first]))