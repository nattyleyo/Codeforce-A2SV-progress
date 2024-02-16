t = int(input())
for _ in range(t):
    bStr = input()
    aStr = ""
    for i in range(0, len(bStr)-1, 2):
        aStr += bStr[i]
    aStr += bStr[-1]
    print(aStr)
