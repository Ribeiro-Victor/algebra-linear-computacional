import math
class Function_Root:

    def __init__(self, c1, c2, c3, c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4

    def get_func_value(self, x):
        try:
            return self.c1*math.exp(self.c2*x) + self.c3*(x**self.c4)
        except OverflowError:
            return float('inf')
    
    def get_derivative_value(self, x):
        try:
            return self.c1*self.c2*math.exp(self.c2*x) + self.c3*self.c4*(x**(self.c4-1))
        except OverflowError:
            return float('inf')

    def bissection_method(self, a, b, maxTolerance):
        f_a = self.get_func_value(a)
        f_b = self.get_func_value(b)
        if((f_a > 0 and f_b > 0) or (f_a < 0 and f_b < 0)):
            return "Erro: Nao e possivel encontrar a raiz no intervalo definido."
        
        if(f_a < 0 and f_b > 0):
            increasing = 1.0
        else:
            increasing = -1.0

        while(abs(a-b) > maxTolerance):
            x = (a+b)/2.0
            f_i = self.get_func_value(x)
            if(f_i*(increasing) > 0):
                b = x
            else:
                a = x
        
        return x

    def newton_method(self, a, b, maxTolerance):
        max_iter = 10000
        x0 = (a+b)/2.0
        for _ in range(max_iter):
            x = x0 - (self.get_func_value(x0) / self.get_derivative_value(x0))
            residue = abs(x-x0)
            if(residue < maxTolerance):
                return x
            x0 = x
        return("Nao converge.")

