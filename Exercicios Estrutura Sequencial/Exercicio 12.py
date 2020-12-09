"""
Problema "retangulo"
Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
da área, perímetro e diagonal deste retângulo.
"""

base = float(input('Digite a basedo retângulo: '))
altura = float(input('Digite a altura do retângulo: '))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = (base * base + altura * altura) ** (1/2)

print(f'Area: {area}')
print(f'Perimetro: {perimetro}')
print(f'Diagonal: {round(diagonal)}')
