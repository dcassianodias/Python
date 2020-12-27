"""
Faça um programa que peça ao usuário digitar 10 valores e some-os.
"""

soma = 0

for n in range (1, 11):
    num = float(input('Informe um valor: '))
    soma = soma + num
print(f'A soma é {soma}')