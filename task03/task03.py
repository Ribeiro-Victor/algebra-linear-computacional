from task03.interpolation import Interpolation
from task03.regression import Regression
import configparser

icod_map = {
    1: Interpolation,
    2: Regression
}
def run():
    with open("task03/input.txt", "r") as file:
        parser_string = '[INPUT]\n' + file.read()
    parser = configparser.ConfigParser()
    parser.read_string(parser_string)
    
    try:
        icod  = int(parser['INPUT']['ICOD'])
        n = int(parser['INPUT']['n'])
        x = int(parser['INPUT']['x'])
        input_path_points = parser['INPUT']['path_points']
        output_path = parser['INPUT']['output']
    except:
        raise Exception("ERROR: Arquivo de input com erro.")

    ChoosenMethod = icod_map[icod]
    points = []
    with open("task03/"+input_path_points, "r") as file:
        content = file.readlines()
        for row in content:
            pair = [float(num) for num in row.split(' ')]
            points.append(pair)

    methodClass = ChoosenMethod(
        n=n,
        points=points,
        x=x
    )

    y = methodClass.solve()
    
    with open("task03/"+output_path, "w") as file:
        buffer = f"f({x}) = {y}"
        file.write(buffer)
    
    print("Task03 executada com sucesso. Saída disponível em: task03/"+output_path)