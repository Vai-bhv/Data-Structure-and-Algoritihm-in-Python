import sys
from math import sqrt
list = []
for line in sys.stdin:
    for i in line.split():
        list.append(int(i))

# print(list)


for i in range (0, len(list)):
    n = list[i]
    count = 0
    # print(n)
    for j in range (2,int(sqrt(n))+1):
        if (n % j == 0):
            # print("oooo1")
            count+=1
            break
        j+=1
    i+=1
    if count>0:
        print("Not prime")
    else:
        print("prime")

