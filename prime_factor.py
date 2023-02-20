val = int(input())
div = 2
res = []
while val>=div :
    if(val%div == 0):
        val = val/div
        res.append(div)
    else:
       div += 1 
 
n = len(res)
count = 1
ans = ''
for i in range(1,n):
    if(res[i-1] == res[i]):
        count += 1
    else:
        if(count > 1):
            ans += str(res[i-1]) + '^' + str(count)
        else:
            ans += str(res[i-1])
        ans += ' * '
        count = 1
if(count > 1):
    ans += str(res[n-1]) + '^' + str(count)
else:
    ans += str(res[n-1])
print(ans)