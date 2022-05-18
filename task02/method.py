class Method:
    allows_determinant_calc = True

    def __init__(self, order, determinant_calc, matrix_A, maxTolerance):
        self.order = order
        self.determinant_calc = determinant_calc
        self.matrix_A = matrix_A
        self.maxTolerance = maxTolerance
    
    def solve(self):
        pass