linhas = []
with open('entrada.txt', 'r') as arq:
    matriz = [[int(num) for num in linha.split(' ')] for linha in arq]

for linha in matriz:
    print(linha)