n = int(input())
s = input()
ans = []
p = 0
for i in range(1,55):
    if p < n:
        ans.append(s[p])
        p += i
print(''.join(ans))

    
    

