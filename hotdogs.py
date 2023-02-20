import sys
l = []
integer = 0
for line in sys.stdin:
    for c in line.split():
        l.append(int(c))
# print(l)
l.sort()
# print(l)
return_index = l[0]
revenue = 0
maximum_revenue = 0
for i in range (len(l)):
    revenue = l[i] * (len(l) - i )
    if (maximum_revenue < revenue):
        maximum_revenue = revenue
        return_index = l[i]
        

print(return_index)