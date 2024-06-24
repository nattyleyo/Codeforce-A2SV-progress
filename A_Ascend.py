n = int(input())
a = list(map(int,input().split()))
stack = []
stack.append(a[0])
ans = 0
for i in range(1,n):
    if stack and stack[-1] >= a[i]:
        ans = max(ans,len(stack))
        stack = []
   
    stack.append(a[i])
ans = max(ans,len(stack))
print(ans)        



# memo = {}
# def dp(i):
#     if i >= n:
#         return 0
#     if i not in memo:
#         memo[i] = 1
#         for j in range(i+1,n):
#             if a[j] > a[i]:
#                 memo[i] = max(1+dp(j),memo[i])
#             else:
#                 break
        
#     return memo[i]
# ans = 0
# for i in range(n):
#     ans = max(ans,dp(i))
    
# print(ans)
        