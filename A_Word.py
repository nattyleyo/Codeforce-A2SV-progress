s = input()
l = 0
u = 0
for c in s:
    if c == c.lower():
        l += 1
    else:
        u += 1
if l >= u:
    print(s.lower())
else:
    print(s.upper())