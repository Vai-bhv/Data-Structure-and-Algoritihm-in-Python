class Matrix:
    def __init__(self,Matrix):
        self.matrix = Matrix
        self.numOfRows = len(Matrix)
        self.numOfColumns = len(Matrix[0])
    def __repr__(self):
        m = ''
        for row in range(0, self.numOfRows):
            for column in range(0, self.numOfColumns):
                m += str(self.matrix[row][column])
                if column != self.numOfColumns - 1:
                    m += ' '
            if row != self.numOfRows - 1:
                m += '\n'
        return m
    def dims(self):
        r = len(self.matrix)
        c = len(self.matrix[0])
        return (r,c)
    def vals(self):
        return self.matrix
    def __add__(self,b):
        resulting_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                sum = self.matrix[i][j] + b.matrix[i][j]
                row.append(sum)
            resulting_matrix.append(row)
        resulting_matrix = Matrix(resulting_matrix)
        return resulting_matrix
    def __sub__(self,b):
        resulting_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                sum = self.matrix[i][j] - b.matrix[i][j]
                row.append(sum)
            resulting_matrix.append(row)
        resulting_matrix = Matrix(resulting_matrix)
        return resulting_matrix
    def __mul__(self,b):
        resulting_matrix =[]
        if type(b) == int:
            for i in self.matrix:
                row = []
                for j in i:
                    row.append(j * b)
                resulting_matrix.append(row)
        else:
            resulting_matrix = zero_matrix2(self.numOfRows, b.numOfColumns)
            for i in range(self.numOfRows):
                row = []
                for j in range(b.numOfColumns):
                    for k in range(b.numOfRows):
                        resulting_matrix[i][j] += self.matrix[i][k] * b.matrix[k][j]
        resulting_matrix = Matrix(resulting_matrix)
        return resulting_matrix

    def is_symmetric(self):
        for i in range(self.numOfRows):
            for j in range(self.numOfColumns):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True


def zero_matrix2(r,c):
    matrix1 = []
    for i in range(r):
        row =[]
        for j in range(c):
            row.append(0)
        matrix1.append(row)
    return matrix1
def zero_matrix(r,c):
    matrix1 = []
    for i in range(r):
        row =[]
        for j in range(c):
            row.append(0)
        matrix1.append(row)
    matrix1 = Matrix(matrix1)
    return matrix1
def identity_matrix(n):
    matrix1 = []
    count = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        row[count] = 1
        count += 1
        matrix1.append(row)
    matrix1 = Matrix(matrix1)
    return matrix1