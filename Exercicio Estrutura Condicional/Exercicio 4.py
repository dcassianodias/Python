"""
Faça um programa q leia um número e, caso ele seja positivo, calcule e mostre:
    O número digitado ao quadrado;
    A raiz quadrada do número digitado
"""

num = float(input('Digite um número: '))

if num > 0:
    print(num ** 2)
    print(f'{num ** (1/2):.2f}')
else:
    print('Número inválido')
