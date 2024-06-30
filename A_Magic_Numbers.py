number = input()

is_magical = True

for char in number:
    if char != '1' and char != '4':
        is_magical = False
        break

if number[0] == '4':
    is_magical = False

if '444' in number:
    is_magical = False

if is_magical:
    print("YES")
else:
    print("NO")
