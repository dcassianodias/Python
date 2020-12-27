"""
Faça um programa que leia 10 inteiros e imprima sua média.
"""

soma = 0

for n in range(1, 6):
    num = int(input('Digite um número: '))
    soma = num + soma
print(f'A soma total dos números digitados é {soma}. A média do total dos números digitados é {soma/5 }')
