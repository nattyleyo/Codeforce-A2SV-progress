import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    
    bonus = [] 
    power = 0

    for card in cards:
        if card == 0:  
            if bonus:
                power += -heapq.heappop(bonus)
        else:
            heapq.heappush(bonus, -card)  
    print(power)
