from math import sqrt
a = int(input())
b = int(input())
c = int(input())
triplet = False
if (c>a and c>b):
    if (c == int(sqrt((a*a)+(b*b)))):
        triplet = True
elif (a>b and a>c):
    if(a == int(sqrt((c*c)+(b*b)))):
        triplet = True
else:
    if(b == int(sqrt((a*a)+(c*c)))):
        triplet = True

if triplet:
    print("true")
else:
    print("false")