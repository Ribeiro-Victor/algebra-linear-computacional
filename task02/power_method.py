from task02.method import Method
from utils.utils import biggest_vector_element, multiply_matrix_vector

class Power_Method(Method):
    allows_determinant_calc = False

    def solve(self):
        
        old_eigenvector = [1.0] * self.order
        old_eigenvalue = 1.0
        iteration = 0
        residue = 1.0

        while(residue > self.maxTolerance):
            iteration +=1
            
            next_eigenvector = multiply_matrix_vector(self.matrix_A, old_eigenvector)

            next_eigenvalue = biggest_vector_element(next_eigenvector)
            
            for i in range(self.order):
                next_eigenvector[i] = next_eigenvector[i]/next_eigenvalue

            residue = abs(next_eigenvalue-old_eigenvalue) / abs(next_eigenvalue)

            #print("iteracao=", iteration)
            #print("x_i=", old_eigenvector, "\tx_i+1=", next_eigenvector)
            #print("\tautovalor=", next_eigenvalue, "\tresiduo=", residue, "\n")
            
            old_eigenvector = next_eigenvector
            old_eigenvalue = next_eigenvalue
        
        if(self.determinant_calc == True):
            print("WARNING: Não é possível calcular o determinante nesse método.")
        
        return {
            "eigenvector": next_eigenvector,
            "eigenvalue": next_eigenvalue,
            "numberofIterations": iteration
        }

