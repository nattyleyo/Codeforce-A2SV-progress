n = int(input())

res = 4444477777
def backtrack(num,four,seven):
    global res
    if num > res:
        return
    if num >= n and four == seven:
        res = min(res,num)
        return
    backtrack(num*10 + 4,four + 1, seven)
    backtrack(num*10 + 7,four, seven + 1)
backtrack(0,0,0)
print(res)