n,k  = list(map(int,input().split()))
even = n//2
odd = n-even
# print(odd,even)
ans = 0
if k > odd:
    ans = 2*(k-odd)
else:
    ans = 2*k-1
print(ans)