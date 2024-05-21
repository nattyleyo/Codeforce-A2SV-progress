s = input().lower()
vowel = set(['a' ,'e' ,'i','o','u','y'])
arr =[]
# print(s)
for c in s:
    if c not in vowel:
        arr.append('.'+c)
        
print(''.join(arr))
