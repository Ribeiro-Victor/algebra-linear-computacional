import copy
from decimal import *
from mailbox import linesep
import math

def read_matrix(file_path):
    with open(file_path, 'r') as f:
        matrix = [[float(num) for num in row.split(' ')] for row in f]
    return matrix

def read_vector(file_path):
    with open(file_path, 'r') as f:
        vector = [float(num) for num in f]
    return vector

def print_matrix(matrix):
    print('\n'.join([''.join(['{:10.3f}'.format(item) for item in row]) 
      for row in matrix]))
    
def print_vector(vector):
    print('\n'.join('{:10.3f}'.format(item) for item in vector))

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

def vector_subtraction(x, y):
    return [x[i]-y[i] for i in range(len(x))]

def vector_euclidean_norm(x):
    return (sum(x[i]**2 for i in range(len(x))))**0.5

def diagonally_dominant(matrix):

    for i in range(len(matrix)):

        line_summation = 0
        column_summation = 0
        
        for j in range(len(matrix)):
            if(i!=j):
                line_summation += abs(matrix[i][j])
                column_summation += abs(matrix[j][i])

        if(abs(matrix[i][i]) < line_summation or abs(matrix[i][i]) < column_summation):
            return False
    
    return True
def multiply_matrix_vector(a, b):
    number_of_rows = len(a)
    number_of_columns = len(b)
    result = [0.0 for _ in range(number_of_columns)] 
    for i in range(number_of_rows):
            for j in range(number_of_columns):
                result[i] += a[i][j] * b[j]
    return result


def multiply_matrixes(a, b):
    number_of_rows = len(a)
    number_of_columns = len(b[0])
    result = [[0.0 for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    for i in range(number_of_rows):
            for j in range(number_of_columns):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
    return result

def biggest_vector_element(vector):
    biggest = vector[0]
    for i in range(len(vector)):
        if(vector[i]>biggest):
            biggest = vector[i]
    return biggest

def biggest_element_outof_diagonal(matrix):
    biggest = -1
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    if(number_of_rows != number_of_columns):
        raise Exception("Nao é possivel calcular para matrizes não quadradas!")
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            if (i!=j and abs(matrix[i][j]) > biggest):
                biggest = abs(matrix[i][j])
                index = [i, j]
    return index

def calculate_p_matrix(matrix_a, index):
    order = len(matrix_a)
    matrix_p = [[0.0 for _ in range(order)] for _ in range(order)]
    for i in range(order):
        matrix_p[i][i] = 1

    phi = math.pi/4
    if(matrix_a[index[0]][index[0]] != matrix_a[index[1]][index[1]]):
        denominator = matrix_a[index[0]][index[0]] - matrix_a[index[1]][index[1]]
        phi = (0.5) * math.atan( (2*matrix_a[index[0]][index[1]]) / denominator )
    
    matrix_p[index[0]][index[1]] = (-1)*math.sin(phi)
    matrix_p[index[1]][index[0]] = math.sin(phi)
    matrix_p[index[0]][index[0]] = math.cos(phi)
    matrix_p[index[1]][index[1]] = math.cos(phi)

    return matrix_p




