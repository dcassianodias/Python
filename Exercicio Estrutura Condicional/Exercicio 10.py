"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas (onde h corresponde a altura);

Homens: (72.7 * h) - 58
Mulheres: (62.1 * h) - 44.7
"""

altura = float(input('Digite a sua altura: '))
sexo = input('Digite seu sexo. Digite m para masculino ou f para feminino: ')

if sexo.lower() == 'm':
    print(f'O seu peso ideal é {(72.7 * altura) - 58:.2f}')
elif sexo.lower() == 'f':
    print(f'O seu peso ideal é {(62.1 * altura) - 44.7:.2f}')
else:
    print('Dados incorretos.Digite novamente !!!')


