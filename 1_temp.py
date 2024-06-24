# class TrieNode:
#     def __init__(self):
#         self.is_end = False
#         self.children = {}
#         self.word = None

#     def addWord(self, word: str) -> None:
#         cur = self.root

#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TrieNode()
#             cur = cur.children[c]
#         cur.is_end = True
#         cur.word = word
        
#     def startsWith2(prefix):
#         cur = root
#         for c in prefix:
#             if c not in cur.children:
#                 return prefix
#             cur = cur.children[c]
#             if cur.is_end:
#                 return cur.word
#         return prefix
        
#     def search(self, word: str) -> bool:

#         cur = self.root

#         for c in word:
#             if c not in cur.children:
#                 return False
#             cur = cur.children[c]
#         if cur.is_end:
#             return True
        
#     def search2(self, word: str) -> bool:
#         que = deque([(0,self.root)])
#         n = len(word)
#         while que:
#             i,node = que.popleft()
#             if i == n:
#                 if node.is_end:
#                     return True
#                 continue
#             c = word[i]
#             if c == '.':
#                 for d in node.children.values():
#                     que.append((i+1,d))
#             else:
#                 if c in node.children:
#                     que.append((i+1,node.children[c]))
#         return False
    
#     def dfs(node):
#         nonlocal ans
#         if node.word:
#             if len(ans) < len(node.word):
#                 ans = node.word
#             elif len(ans) == len(node.word) and ans > node.word:
#                 ans = node.word
#         for child in node.children.values():
#             if child.is_end:
#                 dfs(child)