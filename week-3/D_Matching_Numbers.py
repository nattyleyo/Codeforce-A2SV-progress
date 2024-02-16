t = int(input())
for i in range(t):
    #     1 2 3 4 5 6
    # [1,3] [2,4]==>[1,3,4]
    # [6,5]  ==>[6,5,2]
    n = int(input())
    my_set = set()
    even = []
    odd = []
    flag = True
    pair_2 = []
    if n == 1:
        print('YES')
        print(str(1)+' '+str(2))
    else:
        mid = (2*n+1)//2
        for j in range(1, mid+1):
            if j % 2 == 0:
                even.append(j)
            else:
                odd.append(j)
        pair_1 = odd+even
        for k in range(2*n, mid, -1):
            pair_2.append(k)
        for i in range(mid):
            sum = pair_1[i]+pair_2[i]
            if sum not in my_set:
                my_set.add(sum)
            else:
                flag = False
                break
        if flag == True:
            print('YES')
            for i in range(mid):
                print(str(pair_1[i])+' '+str(pair_2[i]))
        else:
            print('NO')
