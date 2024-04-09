test = int(input())
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
for _ in range(test):
    n ,k= list(map(int,input().split()))
    nums = list(map(int,input().split()))
          
    minim = min(nums)
    maxim = max(nums)
    
    com = nums[0]-k
    for i in range(n):
        com = gcd(com,nums[i]-k)
        if com == 1:
            break
    if com == 0 :
        print(0)
        continue
    if minim <= k <= maxim:
        print(-1)
        continue
    ans  = 0
    for i in range(n):
        part = (nums[i]-k) // com
        ans += abs(part)-1
    # print(nums,com,k)
    print(ans)
        
    
    