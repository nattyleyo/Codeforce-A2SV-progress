from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.word = None
        
def addWord(word):
    cur = root

    for c in word:
        if c not in cur.children:
            cur.children[c] = TrieNode()
        cur = cur.children[c]
    cur.is_end = True
    cur.word = word
        
def startsWith(prefix):
    cur = root
    for c in prefix:
        if c not in cur.children:
            return False
        cur = cur.children[c]
        # if cur.is_end:
        #     return cur.word
    return True

root = TrieNode()

n = int(input())
a = list(map(int,input().split()))
dic = defaultdict(set)
maxi = max(a)
for i in a:
    for j in range(maxi+1):
        b = bin(j)[2:]
        if len(b) <= i:
            dic[i].add(b.zfill(i))
# print(dic)

for d in dic.values():
    addWord(d)

ans = []
cnt = 0
for i in a:
    for j in dic[i]:
        if not startsWith(j):
            if int(j,2) == 0 and i > 1:
                continue
            ans.append(j)
            break

if len(ans):
    if len(set(ans)) == len(ans):
        print('YES')
        for i in ans: 
            print(i)
    else:
        print('NO')
        
else:
    print('NO')

