import sys
input_mat = []
arr = sys.stdin.readline().split(" ")
ar = [v for v in arr if v != ""]
ar = [int(x) for x in ar]
input_mat.append(ar)
for k in range(len(input_mat[0])-1):
    arr = sys.stdin.readline().split(" ")
    ar = [v for v in arr if v != ""]
    ar = [int(x) for x in ar]
    input_mat.append(ar)

list1=[]

for i in range(len(input_mat)):
    for j in range(len(input_mat)):
        if input_mat[i][j] == 0:
            list1 = [i,j]
            break
b = list1[0]
c = list1[1]
if b > 0:
    sum1 = sum(input_mat[0])
else:
    sum1 = sum(input_mat[b-1])
sum0 = sum(input_mat[b])
diff = sum1 - sum0
input_mat[b][c] = diff
p = 0
D1 = 0
D2 = 0
for i in input_mat:
    p += i[c]
flag1 = True
flag2 = True
flag3 = True
for i in range(len(input_mat)):
    D1 += input_mat[i][i]
if D1 != p or p != sum1:
    flag1=False

for i in range(len(input_mat)):
    D2 += input_mat[i][len(input_mat[0])-1-i]
if D2 != p or p != sum1:
    flag2=False

if p != sum1:
    flag3=False
if flag1 and flag2 and flag3:
    for i in input_mat:
        print('\t'.join(map(str, i)))
else:
    print('Can\'t be magic')