import collections
n = int(input())
arr1 = []
for i in range(n):
    arr1.append(input())
# print(arr1)
m = int(input())
arr2 = []
for i in range(m):
    arr2.append(input())
# print(arr2)
# arr = arr1 + arr2
# print(arr)
mydict={}
# making dictionary
for a in arr1:
    key=''.join(sorted(a))
    if key in mydict:
        mydict[key] = mydict[key] + [a]
    else:
        mydict[key]=[a]
# checking for output
for a in arr2:
    key=''.join(sorted(a))
    if key in mydict:
        s = mydict.get(key)
        for c in range(len(s)):
            print(s[c], end=" ")
        print()
    else:
        print('\n')
# print(mydict.values())