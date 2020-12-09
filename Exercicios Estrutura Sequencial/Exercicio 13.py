"""
Problema "idades"
Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
nomes e a idade média entre essas pessoas.
"""

print('Dados da primeira pessoa:\n ')

nome1 = input('Digite o nome: ')
idade1 = int(input('Digite a idade: '))

print('Dados da segunda pessoa:\n ')

nome2 = input('Digite o nome: ')
idade2 = int(input('Digite a idade: '))

media = (idade1 + idade2) / 2

print(f'A média de idade entre {nome1} e {nome2} é {media} anos')
