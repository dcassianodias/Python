"""
Faça um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""

num = int(input('Digite um número: '))
maior = menor = num

for n in range(5):
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f'O maior valor digitado foi {maior} e o menor {menor}')

