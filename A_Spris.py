# n, m = list(map(int, input().split()))
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
a = int(input())
b = int(input())
c = int(input())
ans = 0

x = min(a//1,b//2,c//4)
ans += x * 7 

print(ans)

