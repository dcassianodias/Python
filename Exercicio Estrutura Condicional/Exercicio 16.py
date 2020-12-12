"""
Problema "glicose"
Fazer um programa para ler a quantidade de glicose no sangue de uma pessoa e depois mostrar na tela a
classificação desta glicose de acordo com a tabela de referência ao lado:

// Normal        Até 100 mg/dl
// Elevado       Maior que 100 até 140 mg/dl
//  Diabetes      Maior que 140 mg/d
"""

glicose = int(input('Digite qual o valor da glicose?: '))

if glicose <= 100:
    print('Valor da glicose normal.')
elif glicose <= 140:
    print('Valor da glicose elevada')
else:
    print('Diabetes')
