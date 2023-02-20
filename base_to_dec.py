n = int(input())
b = int(input())
s = list(str(n))
s = s[::-1]
# print(s)
newNumber = 0
for i in range (len(s)):
    count = int(s[i]) * (b**i)
    newNumber += count
    i+=1

print(newNumber)