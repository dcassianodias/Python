"""
Problema "terreno"
Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno.
"""

largura = float(input('Digite a largurado terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
metro_quadrado = float(input('Digite o valor do metro quadrado: '))

area = largura * comprimento
preco = area * metro_quadrado

print(f'Area do terreno: {area}')

print(f'Preco do terreno: {preco}')