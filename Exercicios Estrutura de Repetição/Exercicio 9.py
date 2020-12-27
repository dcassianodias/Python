"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares
"""

soma = 0

for n in range(0, 101):
    print(n)
    if n % 2 == 0:
        soma = n + soma
print(f'A soma dos 50 primeiro números pares é de {soma}')










