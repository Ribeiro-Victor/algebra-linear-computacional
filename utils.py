import copy

def read_matrix(file_path):
    with open(file_path, 'r') as f:
        matrix = [[float(num) for num in row.split(' ')] for row in f]
    return matrix

def print_matrix(matrix):
    print('\n'.join([''.join(['{:10.2f}'.format(item) for item in row]) 
      for row in matrix]))

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