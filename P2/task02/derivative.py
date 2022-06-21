import math
class Derivative:
    
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
    
    def forward_finite_difference(self, x, delta_x):
        return (self.get_func_value(x + delta_x) - self.get_func_value(x)) / delta_x
    
    def backward_finite_difference(self, x, delta_x):
        return (self.get_func_value(x) - self.get_func_value(x - delta_x)) / delta_x

    def central_finite_difference(self, x, delta_x):
        return (self.get_func_value(x + delta_x) - self.get_func_value(x - delta_x)) / (2*delta_x)
    
    def richard_extrapolation(self, x, delta_x1, delta_x2):
        d1 = self.forward_finite_difference(x, delta_x1)
        d2 = self.forward_finite_difference(x, delta_x2)
        q = delta_x1/delta_x2
        return d1 + ((d1-d2)/((q**-1)-1))


