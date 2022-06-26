import numpy as np
import configparser

class NL_System:

    def __init__(self, theta, maxTolerance):
        self.theta = theta
        self.maxTolerance = maxTolerance
        self.error = None
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
                self.error = 'Matriz jacobiana singular, nao pode ser invertida.'
                return x
            delta_x = (-1) * np.matmul(inverse_jacobian, func_matrix)
            x = x + delta_x
            residue = np.linalg.norm(delta_x) / np.linalg.norm(x)

            if (residue < self.maxTolerance):
                return x
        self.error = 'convergence not reached.'
        return x
    
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
                self.error = 'Matriz jacobiana singular, nao pode ser invertida.'
                return x
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
        self.error = 'convergence not reached.'
        return x

    def prova_real(self, solution):
        if(not isinstance(solution, str)):
            experimental = self.get_func_value(solution)
            f1 = experimental[0] + 1
            f2 = experimental[1] + self.theta[0]
            f3 = experimental[2] + self.theta[1]
            print(f'f1 -> 1.0 ~ {f1}')
            print(f'f2 -> {self.theta[0]} ~ {f2}')
            print(f'f3 -> {self.theta[1]} ~ {f3}')


def run():
    
    with open("P2/task01/input.txt", "r") as file:
        parser_string = '[INPUT]\n' + file.read()
    parser = configparser.ConfigParser()
    parser.read_string(parser_string)
    
    try:
        icod  = int(parser['INPUT']['ICOD'])
        theta1 = float(parser['INPUT']['theta1'])
        theta2 = float(parser['INPUT']['theta2'])
        maxTolerance = float(parser['INPUT']['TOLm'])
        output_path = parser['INPUT']['output']
    except:
        raise Exception("ERROR: Arquivo de input com erro.")
    system =  NL_System(theta=[theta1, theta2], maxTolerance=maxTolerance)
    
    solution = []
    if(icod == 1):
        solution = system.newton_method()
    elif(icod == 2):
        solution = system.broyden_method()

    buffer = '-'*20 + 'Dados lidos' + '-'*20 + '\n'
    buffer += f'ICOD = {icod}\nTheta1 = {theta1}\tTheta2 = {theta2}\nTOLm = {maxTolerance}\n'
    buffer += '-'*22 + 'Solucao' + '-'*22 + '\n'
    if(system.error != None):
        buffer += f'[ERRO]{system.error}\n'
    buffer += f'c2 = {solution[0]}\nc3 = {solution[1]}\nc4 = {solution[2]}'
    
    with open("P2/task01/"+output_path, "w") as file:
        file.write(buffer)

    print("P2 - Task01 executada com sucesso. Saída disponível em: P2/task01/"+output_path)
