"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos
"""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O maior número digitado é {num1} e a diferença entre eles é de {num1 - num2} ')
else:
    print(f'O maior número digitado é {num2} e a diferença entre eles é de {num2 - num1}')
