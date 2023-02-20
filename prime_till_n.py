import sys
from math import sqrt
input = []
for line in sys.stdin:
    for i in line.split():
        input.append(int(i))

high = input[1]
low = input[0]

list = [] 
for i in range (low , high+1):
    # print(i)
    n = i 
    count = 0
    # print(n)1
    
    for j in range (2 , int(sqrt(n))+1):
        if (n%j==0):
            count+=1
            break
        # print(i)
        # print(j)
        j+=1    
        # i+=1
    if count > 0:
        pass
    else:
        list.append(n)
    # print(n)
    i+=1
    # print(n)
print(list)

