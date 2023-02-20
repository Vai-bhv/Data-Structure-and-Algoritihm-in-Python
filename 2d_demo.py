n_rows= int(input()) 
 
n_columns = int(input()) 
 
#Define the matrix 
 
matrix = [] 
 
#for user input 
 
for i in range(n_rows):          # A for loop for row entries 
 
    a =[] 
    # print(a)
    for j in range(n_columns):      # A for loop for column entries 
 
        a.append(int(input())) 
    
    matrix.append(a) 
    # print(a)
   
 
#To print the matrix 
 
for i in range(n_rows): 
 
    for j in range(n_columns): 
 
        print(matrix[i][j], end = " ") 
 
    print()