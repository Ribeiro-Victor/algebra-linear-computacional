from task01.method import Method
from utils.utils import backward_substitution, forward_substitution, print_matrix, check_symmetry, transpose_matrix

class Cholesky_Method(Method):
    def decompose(self):
        number_of_rows = len(self.matrix_A)
        number_of_columns = len(self.matrix_A[0])

        if(number_of_columns != number_of_rows):
            raise Exception("ERRO: A matriz deve ser quadrada para realizar este método.")

        if(not check_symmetry(self.matrix_A)):
            raise Exception("ERRO: A matriz deve ser simétrica para realizar este método.")

        for i in range(number_of_rows):
            summation = sum(self.matrix_A[i][k]**2 for k in range(i))
            self.matrix_A[i][i] = self.matrix_A[i][i] - summation
            if(self.matrix_A[i][i] <= 0):
                raise Exception("ERRO: A matriz deve ser positiva definida para realizar este método.")
            else:
                self.matrix_A[i][i] = self.matrix_A[i][i] ** 0.5
            for j in range(i+1, number_of_columns):
                summation = sum(self.matrix_A[i][k]*self.matrix_A[j][k] for k in range(i))
                self.matrix_A[j][i] = (self.matrix_A[i][j] - summation)/self.matrix_A[i][i]
        
        return self.matrix_A

    def solve(self):
        self.decompose()
        #print("Matriz LL^t:")
        #print_matrix(self.matrix_A)
        
        determinant = None
        if (self.determinant_calc):
            determinant = self.calc_determinant()
            print("Determinante: ", determinant)
        
        vector_ly = forward_substitution(self.matrix_A, self.vector_B, flag=False)
        vector_x = backward_substitution(transpose_matrix(self.matrix_A), vector_ly)

        return {
            "vector": vector_x,
            "determinant": determinant}
    
    def calc_determinant(self):
        det = self.matrix_A[0][0]
        for i in range(1, self.order):
            det = det * self.matrix_A[i][i]
        return det**2

