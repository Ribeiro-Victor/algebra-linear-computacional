from task01.method import IterativeMethod
from task01.lu_method import LU_Method
from task01.cholesky_method import Cholesky_Method
from task01.jacobi_method import Jacobi_Method
from task01.gauss_seidel_method import Gauss_Seidel_Method
from utils.utils import read_matrix, read_vector
import configparser

icod_map = {
  1: LU_Method,
  2: Cholesky_Method,
  3: Jacobi_Method,
  4: Gauss_Seidel_Method
}

def run():
    with open("task01/input.txt", "r") as file:
        parser_string = '[INPUT]\n' + file.read()
    parser = configparser.ConfigParser()
    parser.read_string(parser_string)
    
    try:
        order = int(parser['INPUT']['ordem'])
        icod  = int(parser['INPUT']['ICOD'])
        idet = int(parser['INPUT']['IDET'])
        maxTolerance = float(parser['INPUT']['TOLm'])
        input_path_A = parser['INPUT']['path_A']
        input_path_B = parser['INPUT']['path_B']
        output_path = parser['INPUT']['output']
    except:
        raise Exception("ERROR: Arquivo de input com erro.")

    ChoosenMethod = icod_map[icod]
    matrix_A = read_matrix("task01/"+input_path_A)
    vector_B = read_vector("task01/"+input_path_B)

    if(not issubclass(ChoosenMethod, IterativeMethod)):
        maxTolerance = None

    methodClass = ChoosenMethod(
        order=order,
        determinant_calc=(idet>0),
        matrix_A=matrix_A,
        vector_B=vector_B,
        maxTolerance=maxTolerance
    )
    solution = methodClass.solve()
    
    with open("task01/"+output_path, "w") as file:
        file.write(f"Solução(X) do sistema: {solution['vector']}\n")
        file.write(f"Determinante: {solution.get('determinant', 'N/A')}\n")
        file.write(f"Número de iterações para convergência: {solution.get('numberofIterations', 'N/A')}\n")
        file.write(f"Histórico da variação do erro: {solution.get('residues', 'N/A')}\n")
    
    print("Task01 executada com sucesso. Saída disponível em: task01/"+output_path)

    
    
    