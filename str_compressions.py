from collections import defaultdict

string  = "sd"
myDict = {}
for char in string:
    if char in myDict:
        myDict[char]+=1
    else:
        myDict[char]=1

for keys in myDict:
    print(keys+str(myDict[keys]), end="") 