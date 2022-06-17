from decimal import DivisionByZero
from P1.task01.method import Method
from utils.utils import backward_substitution, forward_substitution, print_matrix

class LU_Method(Method):
    def decompose(self):
        number_of_rows = len(self.matrix_A)
        number_of_columns = len(self.matrix_A[0])

        if(number_of_columns != number_of_rows):
            raise Exception("ERRO: A matriz deve ser quadrada para realizar este método.")

        for k in range(number_of_columns):
            for i in range(k+1, number_of_columns):
                try:
                    self.matrix_A[i][k] = self.matrix_A[i][k]/self.matrix_A[k][k]
                except DivisionByZero:
                    raise Exception("ERRO: Pivô nulo. Decomposição LU não é possível sem pivotamento.")

            for j in range(k+1, number_of_columns):
                for i in range(k+1, number_of_columns):
                    self.matrix_A[i][j] = self.matrix_A[i][j]-self.matrix_A[i][k]*self.matrix_A[k][j]
        return self.matrix_A
    
    def solve(self):
        self.decompose()
        #print("Matriz LU:")
        #print_matrix(self.matrix_A)
        
        determinant = None
        if (self.determinant_calc):
            determinant = self.calc_determinant()
            print("Determinante: ", determinant)
        
        vector_ly = forward_substitution(self.matrix_A, self.vector_B)
        vector_x = backward_substitution(self.matrix_A, vector_ly)

        return {
            "vector": vector_x,
            "determinant": determinant}
    
    def calc_determinant(self):
        det = self.matrix_A[0][0]
        for i in range(1, self.order):
            det = det * self.matrix_A[i][i]
        return det

