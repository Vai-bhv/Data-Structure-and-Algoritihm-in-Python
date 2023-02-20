n = int(input("till where u wanna print the series"))
first = 0 
second = 1
for i in range (n-1):
    print(second)
    first , second = second , second+first
