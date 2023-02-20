n = int(input())
b = int(input())

def conversion(a,d):
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

conversion(n,b)