def colTraversal(mat,rows,cols):
#     Write your code here.
    # product = [ [0]*rows for i in range(cols)]
    for j in range (cols):
       for i in range(rows):
        if j%2 == 0 :
            print(mat[i][j])
        else:
            print(mat[rows-i-1][j])

rows = int(input())
cols = int(input())

mat = []
for i in range (rows) :
    a = []
    for j in range (cols) :
        a.append(int(input()))
    mat.append(a)

# for r in mat:
#     print(r)

colTraversal(mat,rows,cols)
        