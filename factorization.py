from math import sqrt
n = int(input())
factor = 2
s = ""
while(factor<=int(sqrt(n))):
    if(n%factor==0):
        s+=f'{factor} '
        n = n//factor
    else:
        factor+=1
s+=str(n)
print(s)
