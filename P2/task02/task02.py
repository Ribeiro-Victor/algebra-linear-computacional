from P2.task02.function_root import Function_Root
from P2.task02.integration import Integration
from P2.task02.derivative import Derivative
import configparser


def run():
    with open("P2/task02/input.txt", "r") as file:
        parser_string = '[INPUT]\n' + file.read()
    parser = configparser.ConfigParser()
    parser.read_string(parser_string)
    
    try:
        icod  = int(parser['INPUT']['ICOD'])
        c1 = float(parser['INPUT']['c1'])
        c2 = float(parser['INPUT']['c2'])
        c3 = float(parser['INPUT']['c3'])
        c4 = float(parser['INPUT']['c4'])
        a = float(parser['INPUT']['a'])
        b = float(parser['INPUT']['b'])
        maxTolerance = float(parser['INPUT']['TOLm'])
        n = int(parser['INPUT']['n'])
        delta_x1 = float(parser['INPUT']['delta_x1'])
        delta_x2 = float(parser['INPUT']['delta_x2'])
        output_path = parser['INPUT']['output']
        if(n<2 or n>10):
            print("ERROR: 'n' deve estar entre 2 e 10.")
            return 
        if(icod<1 or icod>4):
            print("ERROR: ICOD deve estar entre 1 e 4.")
            return
    except:
        raise Exception("ERROR: Arquivo de input com erro.")

    buffer = '-'*20 + 'Dados lidos' + '-'*20 + '\n'
    buffer += f'ICOD = {icod}\n'
    buffer += f'c1 = {c1}\tc2 = {c2}\tc3 = {c3}\tc4 = {c4}\n'
    if(icod == 1):
        solution = Function_Root(c1, c2, c3, c4)
        buffer += f'a = {a}\tb = {b}\n'
        buffer += f'TOLm = {maxTolerance}\n'
        buffer += '-'*22 + 'Solucao' + '-'*22 + '\n'
        buffer += f'Raiz da funcao pelo metodo da bissecao:\t{solution.bissection_method(a, b, maxTolerance)}\n'
        buffer += f'Raiz da funcao pelo metodo de newton:\t{solution.newton_method(a, b, maxTolerance)}\n'
    
    elif(icod == 2):
        solution = Integration(c1, c2, c3, c4)
        buffer += f'a = {a}\tb = {b}\n'
        buffer += f'num de pontos de integracao = {n}\n'
        buffer += '-'*22 + 'Solucao' + '-'*22 + '\n'
        buffer += f'Integral por Quadratura Polinomial:\t{solution.polynomial_quadrature(a, b, n)}\n'
        buffer += f'Integral por Quadratura Gauss-Legendre:\t{solution.legendre_gauss_quadrature(a, b, n)}\n'

    elif(icod == 3):
        solution = Derivative(c1, c2, c3, c4)
        buffer += f'a = {a}\tdelta_x = {delta_x1}\n'
        buffer += '-'*22 + 'Solucao' + '-'*22 + '\n'
        #buffer += f'Derivada analítica:\t\t {Function_Root(c1, c2, c3, c4).get_derivative_value(a)}\n'
        buffer += f'Derivada por Diferenca finita passo a frente:\t{solution.forward_finite_difference(a, delta_x1)}\n'
        buffer += f'Derivada por Diferenca finita passo atras:\t\t{solution.backward_finite_difference(a, delta_x1)}\n'
        buffer += f'Derivada por Diferenca finita passo central:\t\t{solution.central_finite_difference(a, delta_x1)}\n'
    
    else:
        solution = Derivative(c1, c2, c3, c4)
        buffer += f'a = {a}\tdelta_x1 = {delta_x1}\tdelta_x2 = {delta_x2}\n'
        buffer += '-'*22 + 'Solucao' + '-'*22 + '\n'
        buffer += f'Derivada por Extrapolacao de Richard: {solution.richard_extrapolation(a, delta_x1, delta_x2)}\n'

    with open("P2/task02/"+output_path, "w") as file:
        file.write(buffer)
    
    print("P2 - Task02 executada com sucesso. Saída disponível em P2/task02/"+output_path)


