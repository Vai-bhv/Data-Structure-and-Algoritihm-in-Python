num1 = int(input())
num2 = int(input())

def gcd (a,b):
    while(a!=0):
        a , b = b%a , a
        # print(a,b)
    return b
a1 = gcd(num1 , num2)
print(a1)
b1 = ((num1 * num2) // int(a1))
print(b1)
