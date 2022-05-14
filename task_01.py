from decimal import DivisionByZero
from tabnanny import check

from numpy import isin, matrix
from utils import backward_substitution, diagonally_dominant, print_vector, check_symmetry, forward_substitution, read_matrix, print_matrix, matrix_determinant, read_vector, transpose_matrix, vector_euclidean_norm, vector_subtraction
import copy

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

def cholesky_decomposition(matrix):

    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    if(number_of_columns != number_of_rows):
        return "ERRO: A matriz deve ser quadrada para realizar este método."

    if(not check_symmetry(matrix)):
        return "ERRO: A matriz deve ser simétrica para realizar este método."

    #result = copy.deepcopy(matrix)
    result = matrix

    for i in range(number_of_rows):
        summation = sum(result[i][k]**2 for k in range(i))
        result[i][i] = result[i][i] - summation
        if(result[i][i] <= 0):
            return "ERRO: A matriz deve ser positiva definida para realizar este método."
        else:
            result[i][i] = result[i][i] ** 0.5
        for j in range(i+1, number_of_columns):
            summation = sum(result[i][k]*result[j][k] for k in range(i))
            result[j][i] = (result[i][j] - summation)/result[i][i]
    
    return result

def solve_system(matrix, vector, use_lu_method):
    if(use_lu_method):
        matrix_lu = lu_decomposition(matrix)
        if(isinstance(matrix_lu, str)):
            return matrix_lu
        
        vector_ly = forward_substitution(matrix_lu, vector)

        vector_x = backward_substitution(matrix_lu, vector_ly)
        
        return vector_x
    else:
        matrix_lu = cholesky_decomposition(matrix)
        if(isinstance(matrix_lu, str)):
            return matrix_lu
        
        vector_ly = forward_substitution(matrix_lu, vector, flag=False)

        vector_x = backward_substitution(transpose_matrix(matrix_lu), vector_ly)

        return vector_x

def iterative_jacobi(matrix_a, vector_b, tol):

    if(not diagonally_dominant(matrix_a)):
        return "ERROR: Solução não converge, matriz não é diagonal dominante."

    initial_solution = [1.0] * len(vector_b)
    next_solution = [0.0] * len(vector_b)

    residue = 1
    iteration = 0

    result = [[copy.deepcopy(initial_solution), residue]]

    while(residue > tol):

        for i in range(len(next_solution)):
            summation = 0.0

            for j in range(len(next_solution)):
                if(j!=i):
                    summation += (-1)*matrix_a[i][j]*initial_solution[j]
    
            next_solution[i] = round((vector_b[i] + summation)/matrix_a[i][i], 3)

        iteration += 1
        residue = vector_euclidean_norm(vector_subtraction(next_solution, initial_solution))\
                /vector_euclidean_norm(next_solution)
        
        for i in range(len(next_solution)):
            initial_solution[i] = next_solution[i]
        
        result.append([copy.deepcopy(next_solution), residue])

    return result

def iterative_gauss_seidel(matrix_a, vector_b, tol):

    if(not diagonally_dominant(matrix_a)):
        return "ERROR: Solução não converge, matriz não é diagonal dominante."

    initial_solution = [1.0] * len(vector_b)
    next_solution = [0.0] * len(vector_b)

    residue = 1
    iteration = 0

    result = [[copy.deepcopy(initial_solution), residue]]

    while(residue > tol):

        for i in range(len(next_solution)):
            summation = 0.0

            for j in range(len(next_solution)):
                if(j>i):
                    summation += (-1)*matrix_a[i][j]*initial_solution[j]
                if(j<i):
                    summation += (-1)*matrix_a[i][j]*next_solution[j]
    
            next_solution[i] = round((vector_b[i] + summation)/matrix_a[i][i],3)

        iteration += 1
        residue = vector_euclidean_norm(vector_subtraction(next_solution, initial_solution))\
                /vector_euclidean_norm(next_solution)
        
        for i in range(len(next_solution)):
            initial_solution[i] = next_solution[i]
        
        result.append([copy.deepcopy(next_solution), residue])

    return result
        
if __name__ == "__main__":
    #n = int(input("Entre com a ordem do sistema de equacoes: "))
    print("""
    Decomposição LU (ICOD = 1)
    Decomposição de Cholesky (ICOD = 2)
    Procedimento iterativo Jacobi (ICOD = 3)
    Procedimento iterativo Gauss-Seidel (ICOD = 4).
    """)
    icod = int(input("Entre com o ICOD da operacao: "))
    idet = int(input("Entre com o IDET (IDET = 0 não calcula determinante ou maior que 0 calcula o determinante): "))
    matrix_A = read_matrix("matrix5.txt")
    vector_B = read_vector("vector5.txt")
    if(icod == 1):
        x = solve_system(matrix_A, vector_B, use_lu_method=True)
        if(not isinstance(x, str)):
            print_vector(x)
            if(idet > 0):
                det = matrix_A[0][0]
                for i in range(1, len(matrix_A)):
                    det = det * matrix_A[i][i]
                print("Determinante: ", det)
        else:
            print(x)
    if(icod == 2):
        x = solve_system(matrix_A, vector_B, use_lu_method=False)
        if(not isinstance(x, str)):
            print_vector(x)
            if(idet > 0):
                det = matrix_A[0][0]
                for i in range(1, len(matrix_A)):
                    det = det * matrix_A[i][i]
                det = det**2
                print("Determinante: ", det)
        else:
            print(x)


    if(icod == 3 or icod == 4):
        TOLm = float(input("Entre com a tolerancia maxima para solucao iterativa: "))
        if(icod == 3):
            result = iterative_jacobi(matrix_A, vector_B, TOLm)
        else:
            result = iterative_gauss_seidel(matrix_A, vector_B, TOLm)
        if(not isinstance(result, str)):
            for i in range(1, len(result)):
                print("Iteração: ", i)
                print("Vetor x_i  : ", result[i-1][0])
                print("Vetor x_i+1: ", result[i][0])
                print("Residuo: ", "{:.2e}".format(result[i][1]), "\n")
        else:
            print(result)

    






