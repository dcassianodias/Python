"""
Leia um número real. Se o número digitado for positivo imprima a raiz quadrada. Do contrário,
imprima o número ao quadrado
"""

num = float(input('Digite um número real: '))

if num > 0:
    print(f'A raiz quadrada do número digitado é: {num ** (1/2)}')
else:
    print(f'O valor do número digitado ao quadrado é: {num ** 2}')

