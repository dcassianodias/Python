"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""

num = int(input('Digite um número: '))

if num > 0:
    print(f'A raiz quadrada do número digitado é: {num ** (1/2)}')
else:
    print('Número digitado é inválido')
