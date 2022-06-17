# P1 - Task 03

A terceira task é um programa para realizar o cálculo de o valor aproximado de uma função num determinando ponto. Nesse programa, é possível resolver o sistema a partir dos seguintes métodos de solução:

1. Interpolação (ICOD=1)
2. Regressão (ICOD=2)

## Configurando o programa

Antes de executar o programa, é necessário configurar suas entradas no arquivo "input.txt". Este arquivo deve conter os seguintes parâmetros:

- ICOD: Código do método a ser realizado.
- n: Número de pares de pontos (x, y)
- x: Coordenada do ponto que se deseja calcular o valor de y.
- path_points: Caminho do arquivo de entrada da dos pares de pontos.
- output: Caminho do arquivo de saída do programa.

Todos os arquivos de entrada devem estar no diretório <b>task03</b>. Abaixo, temos um exemplo de arquivo texto de input:
```
ICOD = 1
n = 3
x = 15
path_points = points.txt
output = output.txt
```

## Executando o programa

Para executar o programa, basta realizar o procedimento descrito na [página inicial](../../README.md) do projeto.

