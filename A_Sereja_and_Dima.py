n = int(input())
card = list(map(int, input().split()))

turn = True
l,r=0,n-1
a=b=0
while l <= r:
    take = max(card[l],card[r])
    if card[l] <= card[r]:
        if turn:
            a += card[r]
        else:
            b += card[r]
        r -= 1   
    else:
        if turn:
            a += card[l]
        else:
            b += card[l]
        l += 1  
    turn = not turn
print(a,b)