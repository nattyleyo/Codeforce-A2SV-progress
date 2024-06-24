def backtrack(i, comb, Sum):
    global mini
    if Sum == s:
        mini = min(mini, comb[:], key=lambda x: (len(x), x)) if mini else comb[:]
        return
    if Sum > s:
        return
    
    for d in range(i, 10):
        comb.append(d)
        backtrack(d + 1, comb, Sum + d)
        comb.pop()

t = int(input())
for i in range(t):
    s = int(input())
    mini = None        
    backtrack(0, [], 0)
    print(''.join([str(n) for n in mini]))
    
    

    
    
    

