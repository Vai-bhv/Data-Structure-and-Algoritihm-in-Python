n = int(input())
d = int(input())
def digits(a,b):
    count = 0
    # print(a,b)
    while(a%10!=0):
        digits = a%10
        # print(digits)
        if(digits == b):
            # print("")
            count+=1
        a = a//10
    return count

c = digits(n,d)
print(c)