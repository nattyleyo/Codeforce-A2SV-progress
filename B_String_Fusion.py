from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        
def addWord(word):
    cur = root

    for c in word:
        if c not in cur.children:
            cur.children[c] = TrieNode()
        cur = cur.children[c]
        cur.count += 1
    
        

root = TrieNode()

n = int(input())
a = []
total = 0
for i in range(n):
    a.append(input())
    
for i in range(n):
    total += len(a[i])*2
total *= n

for d in a:
    addWord(d)
    
ans = 0
for i in range(n):
    word = a[i][::-1]
    cur = root
    for c in word:
        if c in cur.children:
            cur = cur.children[c]
            ans += cur.count*2
        else:
            break
        
print(total-ans)
        
    
        
    
    
