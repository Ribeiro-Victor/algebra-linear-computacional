# P2 - Task 02

A segunda task é um programa que calcula raizes, integrais e derivadas de uma função por meio de diferentes métodos:

1. Raiz (ICOD=1)
    - Método da Bisseção
    - Método de Newton
2. Integral (ICOD=2)
    - Quadratura Polinomial
    - Quadratura de Gauss-Legendre
3. Derivada (ICOD=3)
    - Diferenças finitas passo a frente
    - Diferenças finitas passo atrás
    - Diferença central
4. Derivada (ICOD=4)
    - Extrapolação de Richard

## Configurando o programa

Antes de executar o programa, é necessário configurar suas entradas no arquivo "input.txt". Este arquivo deve conter os seguintes parâmetros:

- ICOD: Código do método a ser realizado
- c1, c2, c3, c4: Coeficientes da função.
- a, b: Podem ser usados como intervalo para encontrar a raiz ou integração [a,b]. No caso das derivadas, a é o ponto onde procuramos a derivada.
- tolM: Tolerância máxima para a solução iterativa da raiz.
- n: Número de pontos de integração utilizados no cálculo da integral.
- delta_x1, delta_x2: Parâmetros de ajuste para calcular as derivadas.
- output: Caminho do arquivo de saída do programa.

Todos os arquivos de entrada devem estar no diretório <b>task01</b>. Abaixo, temos um exemplo de arquivo texto de input:
```
ICOD = 1
c1 = 1
c2 = 2
c3 = -1
c4 = 4
a = -1
b = 2
TOLm = 0.0001
n = 10
delta_x1 = 0.0001
delta_x2 = 0.0002
output = output.txt
```

## Executando o programa

Para executar o programa, basta realizar o procedimento descrito na [página inicial](../../README.md) do projeto.

