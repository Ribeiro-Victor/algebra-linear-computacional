from task03.interpolation import Interpolation
from task03.regression import Regression

icod_map = {
    1: Interpolation,
    2: Regression
}

if __name__ == "__main__":

    print("""
    Interpolação (ICOD = 1)
    Regressão (ICOD = 2).
    """)
    icod = int(input("Entre com o ICOD da operacao: "))
    ChoosenMethod = icod_map[icod]

    n = int(input("Entre com o número de pares de ponto: "))
    input_path_points = input("Entre com o caminho do arquivo de entrada dos pontos: ")
    points = []
    with open(input_path_points, "r") as file:
        content = file.readlines()
        for row in content:
            pair = [float(num) for num in row.split(' ')]
            points.append(pair)

    x = float(input("Entre com a coordenada(x) do ponto que se deseja calcular o valor de y: "))

    methodClass = ChoosenMethod(
        n=n,
        points=points,
        x=x
    )

    y = methodClass.solve()

    with open('output3.txt', 'w') as file:
        buffer = f"f({x}) = {y}"
        file.write(buffer)
        print(buffer)