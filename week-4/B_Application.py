test = int(input())
my_db = {}
for i in range(test):
    name = input()
    if name not in my_db:
        my_db[name] = 0
        print('OK')
    else:
        my_db[name] += 1
        print(name+str(my_db[name]))
