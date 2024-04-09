from bisect import bisect_left
test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int,input().split()))
    nums = [[nums[idx],idx] for idx in range(len(nums))]
    def merge(leftArr,rightArr):
        left = 0
        right = 0
        res = []
       
        # print(leftArr,rightArr)
        tempLeft = [num[0] for num in leftArr]
        tempright = [num[0] for num in rightArr]
        for i in range(len(leftArr)):
            idx = bisect_left(tempright,tempLeft[i])
            leftArr[i][0] += idx
            
        for i in range(len(rightArr)):
            idx = bisect_left(tempLeft,tempright[i])
            rightArr[i][0] += idx
            
        while left < len(leftArr) and right < len(rightArr):
            if leftArr[left] >= rightArr[right]:
                
                res.append(rightArr[right])
                right += 1
            else:
            
                res.append(leftArr[left])
                left += 1
                
        res.extend(leftArr[left:])
        res.extend(rightArr[right:])
        return res
        
    def mergeSort(left,right):
        if left == right:
            return [nums[left]]
        mid  = (left + right)//2
        leftArr = mergeSort(left,mid)
        rightArr = mergeSort(mid+1,right)
        
        return merge(leftArr,rightArr)
    ans = mergeSort(0,len(nums)-1)
    ans.sort(key=lambda x:x[1])
    ans = [str(num[0]) for num in ans]
    print(' '.join(ans))