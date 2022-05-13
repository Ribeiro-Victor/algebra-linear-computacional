from decimal import DivisionByZero
from utils import read_matrix, print_matrix, matrix_determinant
import copy
import math

def lu_decomposition(matrix):

    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    if(number_of_columns != number_of_rows):
        return "ERRO: A matriz deve ser quadrada para realizar este método." 

    #if(matrix_determinant(matrix)==0):
    #    return("A matriz deve ser não singular para realizar este metodo.")
    
    #result = copy.deepcopy(matrix)
    result = matrix

    for k in range(number_of_columns):
        for i in range(k+1, number_of_columns):
            try:
                result[i][k] = result[i][k]/result[k][k]
            except DivisionByZero:
                return "ERRO: Pivô nulo. Decomposição LU não é possível sem pivotamento."

        for j in range(k+1, number_of_columns):
            for i in range(k+1, number_of_columns):
                result[i][j] = result[i][j]-result[i][k]*result[k][j]

    return result

if __name__ == "__main__":
    n = int(input("Entre com a ordem do sistema de equacoes: "))
    print("""
    Decomposição LU (ICOD = 1)
    Decomposição de Cholesky (ICOD = 2)
    Procedimento iterativo Jacobi (ICOD = 3)
    Procedimento iterativo Gauss-Seidel (ICOD = 4).
    """)
    icod = int(input("Entre com o ICOD da operacao: "))
    idet = int(input("Entre com o IDET (IDET = 0 não calcula determinante ou maior que 0 calcula o determinante): "))
    matrix_A = read_matrix("entrada_A.txt")
    vector_B = read_matrix("entrada_B.txt")
    if(icod == 3 or icod == 4):
        TOLm = float(input("Entre com a tolerancia maxima para solucao iterativa: "))





