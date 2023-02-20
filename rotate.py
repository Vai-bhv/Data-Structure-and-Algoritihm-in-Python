n = int(input())
t = int(input())
quotient = 0
remainder = 0
newNumber = 0 
count = 0
k = n
while(n%10!=0):
    count+=1
    n = n//10
t = t%count
if (t>=0 and k>=0):
    quotient = k // (10**t)
    remainder = k % (10**t)
    newNumber = (remainder * (10**(count-t))) + quotient
else:
    t = abs(t)
    k = abs(k)
    quotient = k // (10**(count -t))
    # print(quotient)
    remainder = k % (10**(count - t))
    # print(remainder)
    newNumber = (remainder * (10**(t))) + quotient

print(newNumber)