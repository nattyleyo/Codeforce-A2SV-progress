from collections import defaultdict,deque
n = int(input())
nums = list(map(int,input().split()))
graph = defaultdict(list)

def inbound()
for i in range(n):
    a,b= 1,0
    while a >= 1:
        graph[i].append(nums[a])
        a = i-nums[i]
    while b <= n:
        graph[i].append(nums[b])
        b = i+nums[i]
        
      
print(graph)