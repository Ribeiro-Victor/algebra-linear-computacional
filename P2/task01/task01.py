import numpy as np

class NL_System:

    def __init__(self, theta, maxTolerance):
        self.theta = theta
        self.maxTolerance = maxTolerance
        pass

    def get_jacobian(self, x):
        c2 = x[0]
        c3 = x[1]
        c4 = x[2]
        line_1 = [2*c2, 4*c3, 12*c4]
        line_2 = [12*c2*c3 + 36*c3*c4, 24*(c3**2) + 6*(c2**2) + 36*c2*c4 + 108*(c4**2), 36*c2*c3 + 216*c3*c4]
        line_3 = [120*c2*(c3**2) + 576*(c3**2)*c4 + 504*c2*(c4**2) + 1296*(c4**3) + 72*(c2**2)*c4 + 3, \
                  240*(c3**3) + 120*(c2**2)*c3 + 1152*c2*c3*c4 + 4464*c3*(c4**2), \
                  576*c2*(c3**2) + 4464*(c3**2)*c4 + 504*(c2**2)*c4 + 3888*c2*(c4**2) + 13392*(c4**3) + 24*(c2**3)]
        return [line_1, line_2, line_3]

    def get_func_value(self, x):
        c2 = x[0]
        c3 = x[1]
        c4 = x[2]
        theta1 = self.theta[0]
        theta2 = self.theta[1]
        f1 = 2*(c3**2) + (c2**2) + 6*(c4**2) - 1
        f2 = 8*(c3**3) + 6*c3*(c2**2) + 36*c3*c2*c4 + 108*c3*(c4**2) - theta1
        f3 = 60*(c3**4) + 60*(c3**2)*(c2**2) + 576*c2*c4*(c3**2) + \
            2232*(c3**2)*(c4**2) + 252*(c4**2)*(c2**2) + 1296*c2*(c4**3) + \
            3348*(c4**4) + 24*(c2**3)*c4 + 3*c2 - theta2
        return [f1, f2, f3]
    
    def newton_method(self):
        x = [1.0, 0.0, 0.0]
        max_iter = 10000

        for _ in range (max_iter):

            jacobian = self.get_jacobian(x)
            func_matrix = self.get_func_value(x)
            try:
                inverse_jacobian = np.linalg.inv(jacobian)
            except:
                return "Matriz jacobiana singular, nao pode ser invertida."
            delta_x = (-1) * np.matmul(inverse_jacobian, func_matrix)
            x = x + delta_x
            residue = np.linalg.norm(delta_x) / np.linalg.norm(x)

            if (residue < self.maxTolerance):
                return x
        return("Nao converge.")
    
    def broyden_method(self):
        x = [1.0, 0.0, 0.0]
        max_iter = 10000
        b_matrix = self.get_jacobian(x)

        for _ in range (max_iter):

            jacobian = b_matrix.copy()
            func_matrix = self.get_func_value(x)
            try:
                inverse_jacobian = np.linalg.inv(jacobian)
            except:
                return "Matriz jacobiana singular, nao pode ser invertida."
            delta_x = (-1) * np.matmul(inverse_jacobian, func_matrix)
            x = x + delta_x
            y =  np.array(self.get_func_value(x)) -  np.array(func_matrix)
            residue = np.linalg.norm(delta_x) / np.linalg.norm(x)

            if (residue < self.maxTolerance):
                return x
            else:
                numerator = np.matmul(y - np.matmul(b_matrix, delta_x), (np.transpose(delta_x)))
                denominator = np.matmul(np.transpose(delta_x), delta_x)
                b_matrix = b_matrix + (numerator/denominator)
        return("Nao converge.")

    def prova_real(self, solution):
        if(not isinstance(solution, str)):
            teorico = self.get_func_value(solution)
            f1 = teorico[0] + 1
            f2 = teorico[1] + self.theta[0]
            f3 = teorico[2] + self.theta[1]
            print(f'f1 -> 1.0 ~ {f1}')
            print(f'f2 -> {self.theta[0]} ~ {f2}')
            print(f'f3 -> {self.theta[1]} ~ {f3}')


def run():
    
    icod = int(input("Entre com o ICOD da operação:"))
    theta1 = float(input("Entre com o teta_1: "))
    theta2 = float(input("Entre com o teta_2: "))
    maxTolerance = float(input("Entre com a tolerância máxima: "))
    system =  NL_System(theta=[theta1, theta2], maxTolerance=maxTolerance)
    
    solution = []
    if(icod == 1):
        solution = system.newton_method()
    elif(icod == 2):
        solution = system.broyden_method()

    if(isinstance(solution, str)):
        buffer = solution
    else:
        buffer = f'c2 = {solution[0]}\nc3 = {solution[1]}\nc4 = {solution[2]}'
    
    with open("P2/task01/output.txt", "w") as file:
        file.write(buffer)

    print("P2 - Task01 executada com sucesso. Saída disponível em: P2/task01/output.txt")
