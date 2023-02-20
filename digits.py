n = int(input())
# digits = len(n)
# print(digits)
count = 0 
while (n%10!=0):
    count+=1
    n = n//10


print(count)

# print(n%10)