# P1 - Task 02

A segunda task é um programa para realizar o cálculo de autovalores e autovetores de uma matriz e calcular o determinante da matriz. Nesse programa, é possível encontrar a solução a partir dos seguintes métodos de solução:

1. Método da Potência (ICOD=1)
2. Método de Jacobi (ICOD=2)

## Configurando o programa

Antes de executar o programa, é necessário configurar suas entradas no arquivo "input.txt". Este arquivo deve conter os seguintes parâmetros:

- ordem: Ordem da matriz de entrada
- ICOD: Código do método a ser realizado
- IDET: Se for 0, não calcula o determinante. Caso seja maior que 0, calcula o determinante.
- TOLm: Tolerância máxima para a solução.
- path_A: Caminho do arquivo de entrada da Matriz A.
- output: Caminho do arquivo de saída do programa.

Todos os arquivos de entrada devem estar no diretório <b>task02</b>. Abaixo, temos um exemplo de arquivo texto de input:
```
ordem = 3
ICOD = 1
IDET = 1
TOLm = 0.01
path_A = matrix.txt
output = output.txt
```

## Executando o programa

Para executar o programa, basta realizar o procedimento descrito na [página inicial](../../README.md) do projeto.

