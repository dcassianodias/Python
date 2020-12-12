"""
Problema "baskara"
Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem.
"""

a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))

delta = (b ** 2) - 4 * a * c

if a == 0 or delta < 0:
    print('Esta equação não possui raizes reais.')
else:
    x1 = (-b + (delta ** (1/2) / (2 * a)))
    x2 = (-b - (delta ** (1/2) / (2 * a)))
    print(f'{x1:.4f}')
    print(f'{x2:.4f}')
