"""
Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais,
imprima a mensagem Números Iguais.
"""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O maior número digitado foi {num1}')
elif num1 == num2:
    print('Os dois números são iguais')
else:
    print(f'O maior número digitado é {num2}')

