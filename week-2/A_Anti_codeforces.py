code = 'codeforces'
t = int(input())
my_list = []
for i in range(t):
    s = input()
    for j in range(len(s)):
        if s[j] != code[j]:
            my_list.append(s[j])
    print(len(my_list))
    my_list = []
