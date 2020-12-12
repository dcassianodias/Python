"""
Problema "dardo"
No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual
foi a maior.
"""

dardo1 = float(input('Digite a distância do primeiro dardo: '))
dardo2 = float(input('Digite a distância do segundo dardo: '))
dardo3 = float(input('Digite a distância do terceiro dardo: '))

if dardo1 > dardo2 and dardo1 >dardo3:
    maior = dardo1
elif dardo2 > dardo3:
    maior = dardo2
else:
    maior = dardo3
    print(f'O dardo que foi lançado mais longe foi o {maior}')

