#approch-1

# def gcd(a,b):
#     if b == 0:
#         return a
#     return gcd(b,a%b)
# a,b = list(map(int,input().split()))
# ans= 0
# for a in range(a,b+1):
#     ans = gcd(ans,a)
#     if ans == 1:
#         break
# print(ans)

# approch-2

# a,b=map(int,input().split())
# if a==b:
#     print(a)
# else:
#     print(1)