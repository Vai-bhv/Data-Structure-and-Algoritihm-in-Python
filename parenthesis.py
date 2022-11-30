import sys
def brack(s,o,c,n,ans):
    if(o==n and c==n):
        ans.append(s)
    if(o<n):
        brack(s+"(",o+1,c,n,ans)
    if(c<o):
        brack(s+")",o,c+1,n,ans)


n = int(sys.stdin.readline())
ans = []

brack("",0,0,n,ans)

for s in ans:
    print(s)