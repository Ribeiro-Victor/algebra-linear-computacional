import copy

def read_matrix(file_path):
    with open(file_path, 'r') as f:
        matrix = [[float(num) for num in row.split(' ')] for row in f]
    return matrix

def read_vector(file_path):
    with open(file_path, 'r') as f:
        vector = [float(num) for num in f]
    return vector

def print_matrix(matrix):
    print('\n'.join([''.join(['{:10.2f}'.format(item) for item in row]) 
      for row in matrix]))
    
def print_vector(vector):
    print('\n'.join('{:10.2f}'.format(item) for item in vector))

def matrix_determinant(matrix):
    #Calcula determinante a partir da expansao de cofatores

    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    result = 0

    if(number_of_rows != number_of_columns):
        return "Nao e possivel calcular o determinante de uma matriz nao quadrada!"

    if(number_of_rows == 1):
        return matrix[0][0]

    for j in range(number_of_columns):
        result += matrix[0][j] * ((-1)**j) * matrix_determinant(get_auxiliar_matrix(matrix, j))

    return result

def get_auxiliar_matrix(matrix, j):
    auxiliar = copy.deepcopy(matrix)

    auxiliar = auxiliar[1:]

    for row in range(len(auxiliar)):
        auxiliar[row] = auxiliar[row][:j] + auxiliar[row][j+1:]

    return auxiliar

def check_symmetry(matrix):

    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    if(number_of_rows != number_of_columns):
        return False

    for i in range(number_of_rows):
        for j in range(number_of_columns):
            if(matrix[i][j]!=matrix[j][i]):
                return False
    
    return True

def forward_substitution(matrix_l, vector_b, flag=True):
    #Flag utilizada para indicar que a matrix_l é diagonal inferior
    #mas sua diagonal está "suja" com outros termos da matriz A
    
    number_of_rows = len(matrix_l)
    number_of_columns = len(matrix_l[0])
    vector_x = [0.0] * number_of_columns

    if(flag):
        vector_x[0] = vector_b[0]
    else:
        vector_x[0] = vector_b[0]/matrix_l[0][0]

    for i in range(1, number_of_rows):
        summation = sum(matrix_l[i][j] * vector_x[j] for j in range(i))

        if(flag):
            vector_x[i] = (vector_b[i] - summation)
        else:
            vector_x[i] = (vector_b[i] - summation)/matrix_l[i][i]
    
    return vector_x

def backward_substitution(matrix_u, vector_b):
    
    number_of_rows = len(matrix_u)
    number_of_columns = len(matrix_u[0])
    vector_x = [0.0] * number_of_columns

    vector_x[number_of_columns-1] = vector_b[number_of_columns-1]/matrix_u[number_of_rows-1][number_of_columns-1]

    for i in range(number_of_rows-2, -1, -1):
        summation = sum(matrix_u[i][j] * vector_x[j] for j in range(i+1, number_of_columns))

        vector_x[i] = (vector_b[i] - summation)/matrix_u[i][i]
    
    return vector_x

def transpose_matrix(matrix):
    result = [[0.0] * len(matrix) for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]

    return result


