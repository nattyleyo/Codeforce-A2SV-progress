from heapq import heapify,heappop,heappush
n = int(input())
heap = []
ans = []
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        heappush(heap,int(cmd[1]))
        
    elif cmd[0] == 'getMin':
        x = int(cmd[1])
        while heap and x > heap[0]:
            heappop(heap)
            ans.append('removeMin')
        if not heap or x < heap[0]:
            ans.append('insert '+ str(cmd[1]))         
            heappush(heap,x)
    else:
        if heap:
            heappop(heap)
        else:
            ans.append('insert 1')
    ans.append(' '.join(cmd))         
size = len(ans)
print(size)
for i in range(size):
    print(ans[i])
        