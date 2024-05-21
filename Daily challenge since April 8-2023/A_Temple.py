from collections import defaultdict
# for input 
'''
4
3 2,3 1,2 0,5
1 2,5
0
2 3,1

n = int(input())
dic = defaultdict(list)
for i in range(n):
    node = list(input().split())
    for j in range(1,len(node)):
        a,w=list(map(int,node[j].split(',')))
        dic[node[0]].append((a,w))
print(dic)
'''
'''
input=
3
1 2 2
2 3 1
4 1 4
'''
# edge = int(input())
# dic = defaultdict(list)
# for i in range(edge):
#     a,b,w=list(map(int,input().split()))
#     dic[a].append((b,w))
# print(dic)
dic = defaultdict(list)



    




        
    