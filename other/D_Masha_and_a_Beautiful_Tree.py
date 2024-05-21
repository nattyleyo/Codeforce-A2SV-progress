
test = int(input())

def divide(nums,left,right):
    if left == right:
        return
    
    mid = (left + right)//2
        
    maxi = max(nums[left:mid+1])uuuu
    mini = min(nums[mid+1:right+1])
    
    if maxi > mini:
        global count
        count += 1
        nums[left:mid+1],nums[mid+1:right+1] = nums[mid+1:right+1],nums[left:mid+1]
   
    divide(nums,left,mid)
    divide(nums,mid+1,right)
    
for _ in range(test):
    m = int(input())
    nums = list(map(int,input().split()))
    left = 0
    right = len(nums)-1
    count = 0
    divide(nums,left,right)
    # print(nums)
    if nums == sorted(nums):
        print(count)
    else:
        print(-1)
    