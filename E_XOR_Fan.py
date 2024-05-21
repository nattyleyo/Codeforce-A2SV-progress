test = int(input())
for _ in range(test):
    n = int(input())
    a = list(map(int,input().split()))
    s = input()
    q = int(input())
    pref = [0]*(n+1)

    one,zero = 0,0
    for i in range(n):
        pref[i+1] = pref[i] ^ a[i]
        if s[i] == '0':
            zero ^= a[i]
        else:
            one ^= a[i]
    # print(pref,zero,one)
    for i in range(q):
        cmd = list(map(int,input().split()))
        if cmd[0] == 2:
            tp,bit = cmd
            xor = 0
            if bit == 0:
                print(zero,end=' ')
            else:
                print(one,end=' ')
            
        else:
            tp,l,r = cmd
            x = pref[r] ^ pref[l-1]
            one ^= x
            zero ^= x
    print()
            
            
            
            
        
         