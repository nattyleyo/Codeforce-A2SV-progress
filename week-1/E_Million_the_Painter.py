N = int(input())
s = input()

if ("CC" in s) or ("YY" in s) or ("MM" in s):
    print("No")
elif ("??" in s) or ("C?C" in s) or ("Y?Y" in s) or ("M?M" in s) or (s[0] == "?") or (s[-1] == "?"):
    print("Yes")
else:
    print("No")
