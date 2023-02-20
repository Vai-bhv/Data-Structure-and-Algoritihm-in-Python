n = int(input())
base1 = int(input())
base2 = int(input())

def conversion1(n , b):
    s = list(str(n))
    s = s[::-1]
    # print(s)
    newNumber = 0
    for i in range (len(s)):
        count = int(s[i]) * (b**i)
        newNumber += count
        i+=1
    return newNumber

def conversion2(a,d):
    c = 1
    s = " "
    if(a>1):
        while (a!=0):
            c = a % d
            a = a // d
            s = s + str(c)
        print(s[::-1])
    elif(a == 0):
        print("0")
    else:
        print(c)

a = conversion1(n , base1)
conversion2(a,base2)