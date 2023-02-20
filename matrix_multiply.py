rows1 = int(input())
colomn1 = int(input())
matrix1 = []
for i in range(rows1):
    a1 = []
    for j in range(colomn1):
        a1.append(int(input()))
    matrix1.append(a1)
# for r in matrix1:
#     print(r)



rows2 = int(input())
colomn2 = int(input())
matrix2 = []
for i in range(rows2):
    a2 = []
    for j in range(colomn2):
        a2.append(int(input()))
    matrix2.append(a2)
# for r in matrix2:
#     print(r)




if colomn1 != rows2 :
    print("Invalid input")
    quit()



product = [ [0]*colomn2 for i in range(rows1)]
# for r in product:
#     print(r)
for i in range(rows1):
    for j in range(colomn2):
        for k in range(rows2):
            product[i][j] += matrix1[i][k] * matrix2[k][j]


# for r in product:
#     print(r)
for i in range(rows1):
    for j in range(colomn2):
        print(product[i][j], end=" ")
    print("")