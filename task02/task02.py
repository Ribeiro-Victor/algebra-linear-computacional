from task02.jacobi_method import Jacobi_Method
from task02.power_method import Power_Method
from utils.utils import read_matrix
import configparser

icod_map = {
  1: Power_Method,
  2: Jacobi_Method,
}

def run():
    with open("task02/input.txt", "r") as file:
        parser_string = '[INPUT]\n' + file.read()
    parser = configparser.ConfigParser()
    parser.read_string(parser_string)
    
    try:
        order = int(parser['INPUT']['ordem'])
        icod  = int(parser['INPUT']['ICOD'])
        idet = int(parser['INPUT']['IDET'])
        maxTolerance = float(parser['INPUT']['TOLm'])
        input_path_A = parser['INPUT']['path_A']
        output_path = parser['INPUT']['output']
    except:
        raise Exception("ERROR: Arquivo de input com erro.")

    ChoosenMethod = icod_map[icod]
    matrix_A = read_matrix("task02/"+input_path_A)

    methodClass = ChoosenMethod(
        order=order,
        determinant_calc=(idet>0),
        matrix_A=matrix_A,
        maxTolerance=maxTolerance
    )
    solution = methodClass.solve()
    
    with open("task02/"+output_path, "w") as file:
        file.write(f"Autovalores: {solution['eigenvalue']}\n")
        file.write(f"Autovetores: {solution['eigenvector']}\n")
        file.write(f"Determinante: {solution.get('determinant', 'N/A')}\n")
        file.write(f"Número de iterações para convergência: {solution.get('numberofIterations', 'N/A')}\n")
    
    print("Task02 executada com sucesso. Saída disponível em: task02/"+output_path)
