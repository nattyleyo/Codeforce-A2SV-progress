x = int(input())
count = 0
for i in range(x.bit_length()):
    if x&(1<<i):
        count += 1
print(count)