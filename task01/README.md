# Task 01

A primeira task é um programa para realizar a solução de um sistema de equações lineares e calcular o determinante da matriz nos procedimentos não iterativos. Nesse programa, é possível resolver o sistema a partir dos seguintes métodos de solução:

1. Decomposição LU (ICOD=1)
2. Decomposição de Cholesky (ICOD=2)
3. Procedimento iterativo Jacobi (ICOD=3)
4. Procedimento iterativo Gauss-Seidel (ICOD=4)

## Configurando o programa

Antes de executar o programa, é necessário configurar suas entradas no arquivo "input.txt". Este arquivo deve conter os seguintes parâmetros:

- ordem: Ordem da matriz de entrada
- ICOD: Código do método a ser realizado
- IDET: Se for 0, não calcula o determinante. Caso seja maior que 0, calcula o determinante.
- TOLm: Tolerância máxima para a solução iterativa.
- path_A: Caminho do arquivo de entrada da Matriz A.
- path_B: Caminho do arquivo de entrada do Vetor B.
- output: Caminho do arquivo de saída do programa.

Todos os arquivos de entrada devem estar no diretório <b>task01</b>. Abaixo, temos um exemplo de arquivo texto de input:
```
ordem = 3
ICOD = 4
IDET = 0
TOLm = 0.001
path_A = matrix.txt
path_B = vector.txt
output = output.txt
```

## Executando o programa

Para executar o programa, basta realizar o procedimento descrito na [página inicial](../README.md) do projeto.

