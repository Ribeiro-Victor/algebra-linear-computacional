from task_01 import solve_system

def linear_regression(points, x, n):
    matrix_A = [[0.0] * 2 for _ in range(2)]
    vector_C = [0.0, 0.0]

    matrix_A[0][0] = n
    for i in range(n):
        matrix_A[0][1] += points[i][0]
        matrix_A[1][0] += points[i][0]
        matrix_A[1][1] += points[i][0] ** 2
        vector_C[0] += points[i][1]
        vector_C[1] += points[i][0] * points[i][1]

    vector_X = solve_system(matrix_A, vector_C, use_lu_method=True)
    if(vector_X[0] >=0):
        print("Reta encontrada:", vector_X[1], "x +", vector_X[0])
    else:
        print("Reta encontrada:", vector_X[1], "x -", abs(vector_X[0]))
    
    return vector_X[0] + vector_X[1] * x

def lagrange_interpolation(points, x, n):

    phi = 1.0
    y = 0.0
    for i in range(n):
        for k in range(n):
            if(k!=i):
                phi *= (x - (points[k][0])) / (points[i][0] - points[k][0])
        
        y += phi * points[i][1]
        phi = 1.0
    
    return y
    
if __name__ == "__main__":

    print("""
    Interpolação (ICOD = 1)
    Regressão (ICOD = 2).
    """)
    icod = int(input("Entre com o ICOD da operacao: "))
    n = int(input("Entre com o número de pares de ponto: "))
    points = []
    with open('points.txt', 'r') as file:
        content = file.readlines()
        for row in content:
            pair = [float(num) for num in row.split(' ')]
            points.append(pair)
    x = float(input("Entre com a coordenada(x) do ponto que se deseja calcular o valor de y: "))

    if(icod==1):
        y = lagrange_interpolation(points, x, n)
    elif(icod==2):
        y = linear_regression(points, x ,n)
    else:
        y = "ICOD inválido."
    
    with open('output3.txt', 'w') as file:
        buffer = f"f({x}) = {y}"
        file.write(buffer)
        print(buffer)

    
