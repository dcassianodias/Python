"""
Loop for

Loop -> Estrutura de repetição;
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i <10; i++){
    //execução do loop
}

Python

for item in iteravel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplo de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 2, 3, 4]
- Range
    números = range (1, 10)

#Exemplo de for 1 (Iterenado em ums String)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando em uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range (valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 -> Não

for numero in range(1, 10):
    print(numero)

Enumerate:

((o, 'G'), (1, 'e'), (2, 'e'), (2, 'k')...)

for indice, letra enumerate(nome):
    print(nome[indice])

for i, letra enumerate(nome):
    print(letra)

for _, letra enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_).

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[1])
    
qtd = int(input('Quantas vezes o loop deve acontecer? ))
soma = 0

for n in range (1, qtd +1)
    num = int(input('Informe 0 {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Tebela de emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

# Original: U+1F60D
# Modificado: U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)









