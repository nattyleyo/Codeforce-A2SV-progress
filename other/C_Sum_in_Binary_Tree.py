test = int(input())
for _ in range(test):
    num = int(input())
    total = num

    def findPath(num):
        if num == 1:
            return 1
        return num + findPath(num//2)
    print(findPath(num))
