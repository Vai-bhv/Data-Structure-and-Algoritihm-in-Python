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
oogabooga={}
# making dictionary
for t in arr1:
    key=''.join(sorted(t))
    if key in oogabooga:
        oogabooga[key] = oogabooga[key] + [t]
    else:
        oogabooga[key]=[t]
# checking for output
def omae(*t):
    itera = list(t)
    itera[0].sort()
    print(*itera[0])
for t in arr2:
    key=''.join(sorted(t))
    if key in oogabooga:
        omae(oogabooga[key])
    else:
        print('')