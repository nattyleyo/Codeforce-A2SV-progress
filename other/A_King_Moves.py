cd = input()
c = cd[0]
d = cd[1]
if (d == '1' or d == '8') and (c == "a" or c == "h"):
    print(3)
elif (d != '1' or d != '8') and (c != 'a' or c != 'h'):
    print(8)
else:
    print(5)
