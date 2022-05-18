class Method:
    allows_determinant_calc = True

    def __init__(self, order, determinant_calc, matrix_A, vector_B, **kwargs):
        self.order = order
        self.determinant_calc = determinant_calc
        self.matrix_A = matrix_A
        self.vector_B = vector_B
        if (self.determinant_calc and not self.allows_determinant_calc):
            print("WARNING: Não é possível calcular o determinante nessa decomposição.")
    
    def solve(self):
        pass

class IterativeMethod(Method):
    allows_determinant_calc = False

    def __init__(self, order, determinant_calc, matrix_A, vector_B, maxTolerance):
        self.maxTolerance = maxTolerance
        super().__init__(order, determinant_calc, matrix_A, vector_B)
        
        