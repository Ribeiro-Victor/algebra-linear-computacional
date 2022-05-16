from task_01 import solve_system

def linear_regression(points):
    matrix_A = [[0.0] * 2 for _ in range(2)]
    vector_C = [0.0, 0.0]

    matrix_A[0][0] = len(points)
    for i in range(len(points)):
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
    
    return vector_X

def lagrange_interpolation(points, x, n):

    phi_functions = [0.0] * n
    for i in range(n):

        numerator_product = 1.0
        denominator_product = 1.0

        for k in range(n):
            
            if(k!=i):
                numerator_product *= x - (points[k][0])
                denominator_product *= (points[i][0]) - (points[k][0])
        
        phi_functions[i] = (numerator_product/denominator_product)
    
    return sum(phi_functions[i] * points[i][1] for i in range(n))
    
if __name__ == "__main__":

    
    linear_regression([[1.0,2.0],[2.0,3.5],[3.0,6.5]])
    print(lagrange_interpolation([[-2, -27], [0,-1], [1, 0]], 10, 3))
