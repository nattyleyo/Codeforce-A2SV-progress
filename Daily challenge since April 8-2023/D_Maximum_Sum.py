from collections import defaultdict,deque
test = int(input())
for _ in range(test):
    n,k = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    nums.sort()
    n = len(nums)
    Sum = sum(nums)
    
    queue = deque(nums)
    
    while k > 0:
        maxi = max(queue)
        miniss = [queue[i] for i in range(k+1)]
        minis = sum([queue[i] for i in range(k)])
        print(queue,maxi,miniss,k)
        if maxi <= minis:
            Sum -= queue.pop()
        else:
            Sum -= queue.popleft()
            Sum -= queue.popleft()
        
        k -= 1
      
    print(Sum)
    
        
