s = input()
ans = set()
for c in s:
  ans.add(c)
    
if len(ans)%2 == 0:  
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')