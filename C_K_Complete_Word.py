from collections import defaultdict,Counter
t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    s = list(input())
    count = 0
    size = (k+1)//2
    for i in range(size): 
        freq = defaultdict(int)
        for j in range(i, n, k):
            freq[s[j]] += 1
            if i != k-i-1:  
                freq[s[j + k-2*i-1]] += 1
        
        c = (n // k) * 2 if i != k - 1 - i else (n // k)
        maxi = max(freq.values())
        count += c - maxi
    print(count)      
    
    
    