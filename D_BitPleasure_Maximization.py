class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(2)]
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()

        def insert(num) -> None:
            cur = root
            arr = bin(num)[2:].zfill(32)
            # print(arr)
            for i in range(32):
                b = int(arr[i])
                if not cur.children[b]:
                    cur.children[b] = TrieNode()
                cur = cur.children[b]

        for num in nums:
            insert(num)

        ans = float('-inf')

        for num in nums:    
            cur = root
            arr = bin(num)[2:].zfill(32)

            temp = []

            for i in range(32):
                b = int(arr[i])
                if cur.children[1-b]:
                    temp.append(1-b)
                    cur = cur.children[1-b]
                else:
                    temp.append(b)
                    cur = cur.children[b]
                    
            print(temp)
            
            # bit = ''.join([str(x) for x in temp])

        
            # ans = max(ans,int(bit,2))
            
        
        return ans

        
        
        
# approach - 1
# class TrieNode:
#     def __init__(self):
#         self.is_end = False
#         self.children = [None for i in range(2)]
# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         root = TrieNode()

#         def insert(num) -> None:
#             cur = root

#             num = str(bin(num)[2:])
#             a = 32 - len(num)
#             arr = [0]*a + list(map(int,num))

#             # print(arr)
#             for b in range(32):
        
#                 if not cur.children[arr[b]]:
#                     cur.children[arr[b]] = TrieNode()
#                 cur = cur.children[arr[b]]

#         for num in nums:
#             insert(num)

#         ans = float('-inf')

#         for num in nums:
            
#             cur = root

#             num = str(bin(num)[2:])
#             a = 32 - len(num)
#             arr = [0]*a + list(map(int,num))
#             temp = [0]*32

#             for i in range(32):
#                 b = arr[i]
#                 if cur.children[1-b]:
#                     temp[i] = 1-b
#                     cur = cur.children[1-b]
#                 else:
#                     temp[i] = b
#                     cur = cur.children[b]


#             for i in range(32):
#                 temp[i] ^= arr[i] 
            
#             bit = ''.join([str(x) for x in temp])

        
#             ans = max(ans,int(bit,2))
            
        
#         return ans

        
        
        