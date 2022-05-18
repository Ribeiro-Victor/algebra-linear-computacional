from task02.method import Method
from utils.utils import check_symmetry, multiply_matrixes, biggest_element_outof_diagonal, calculate_p_matrix, transpose_matrix

class Jacobi_Method(Method):

    def solve(self):
        
        if(not check_symmetry(self.matrix_A)):
            raise Exception("ERROR: Não é possível utilizar o método de Jacobi, matriz não é simétrica.")

        matrix_x = [[0.0 for _ in range(self.order)] for _ in range(self.order)]
        for i in range(self.order):
            matrix_x[i][i] = 1
        
        index = biggest_element_outof_diagonal(self.matrix_A)

        iteration = 0
        while(abs(self.matrix_A[index[0]][index[1]]) > self.maxTolerance):
            iteration +=1

            matrix_p = calculate_p_matrix(self.matrix_A, index)
            matrix_pt = transpose_matrix(matrix_p)

            self.matrix_A = multiply_matrixes(matrix_pt, self.matrix_A)
            self.matrix_A = multiply_matrixes(self.matrix_A, matrix_p)

            matrix_x = multiply_matrixes(matrix_x, matrix_p)
            
            index = biggest_element_outof_diagonal(self.matrix_A)

        eigenvalues = []
        for i in range(self.order):
            eigenvalues.append(self.matrix_A[i][i])
        
        determinant = None
        if (self.determinant_calc == True):
            determinant = 1
            for i in eigenvalues:
                determinant *= i
        
        return {
            "eigenvector": transpose_matrix(matrix_x),
            "eigenvalue": eigenvalues,
            "numberofIterations": iteration,
            "determinant": determinant
        }

