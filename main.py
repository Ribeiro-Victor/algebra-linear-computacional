from task01.method import IterativeMethod
from task01.lu_method import LU_Method
from task01.cholesky_method import Cholesky_Method
from task01.jacobi_method import Jacobi_Method
from task01.gauss_seidel_method import Gauss_Seidel_Method
from utils import print_matrix, print_vector, read_matrix, read_vector

icod_map = {
  1: LU_Method,
  2: Cholesky_Method,
  3: Jacobi_Method,
  4: Gauss_Seidel_Method
}

if __name__ == "__main__":
    order = int(input("Entre com a ordem do sistema de equacoes: "))

    print("""
    Decomposição LU (ICOD = 1)
    Decomposição de Cholesky (ICOD = 2)
    Procedimento iterativo Jacobi (ICOD = 3)
    Procedimento iterativo Gauss-Seidel (ICOD = 4).
    """)
    icod = int(input("Entre com o ICOD da operacao: "))
    ChoosenMethod = icod_map[icod]

    idet = int(input("Entre com o IDET (IDET = 0 não calcula determinante ou maior que 0 calcula o determinante): "))
    
    input_path_A = input("Entre com o caminho do arquivo de entrada da matriz A: ")
    matrix_A = read_matrix(input_path_A)
    input_path_B = input("Entre com o caminho do arquivo de entrada do vetor B: ")
    vector_B = read_vector(input_path_B)

    maxTolerance = None
    if(issubclass(ChoosenMethod, IterativeMethod)):
        maxTolerance = float(input("Entre com a tolerância máxima para a solução: "))
    
    print("Matriz A:")
    print_matrix(matrix_A)
    print("Vetor B:")
    print_vector(vector_B)

    methodClass = ChoosenMethod(
        order=order,
        determinant_calc=(idet>0),
        matrix_A=matrix_A,
        vector_B=vector_B,
        maxTolerance=maxTolerance
    )
    solution = methodClass.solve()
    
    with open("output.txt", "w") as file:
        file.write(f"Solução(X) do sistema: {solution['vector']}\n")
        file.write(f"Determinante: {solution.get('determinant', 'N/A')}\n")
        file.write(f"Número de iterações para convergência: {solution.get('numberofIterations', 'N/A')}\n")
        file.write(f"Histórico da variação do erro: {solution.get('residues', 'N/A')}\n")

    
    
    