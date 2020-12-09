"""
Problema "medidas"
Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C
"""

A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))

quadrado = A * A
triangulo_retangulo = (A * B)/2
trapezio = (A + B) * C/2

print(f'A área do quadrado é: {round(quadrado, 4)}')
print(f'A área do triangulo retangulo é: {round(triangulo_retangulo, 4)}')
print(f'A área do trapézio é: {round(trapezio, 4)}')
