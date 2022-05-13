from utils import read_matrix, print_matrix

n = int(input("Entre com a ordem do sistema de equacoes: "))
print("""
Decomposição LU (ICOD = 1)
Decomposição de Cholesky (ICOD = 2)
Procedimento iterativo Jacobi (ICOD = 3)
Procedimento iterativo Gauss-Seidel (ICOD = 4).
""")
icod = int(input("Entre com o ICOD da operacao: "))
idet = int(input("Entre com o IDET (IDET = 0 não calcula determinante ou maior que 0 calcula o determinante): "))
matrix_A = read_matrix("entrada_A.txt")
vector_B = read_matrix("entrada_B.txt")
if(icod == 3 or icod == 4):
    TOLm = float(input("Entre com a tolerancia maxima para solucao iterativa: "))





