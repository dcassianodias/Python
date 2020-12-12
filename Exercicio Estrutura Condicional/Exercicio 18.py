"""
Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa.
Para isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala
vai ser informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra
escala com duas casas decimais. A seguir é dada a fórmula para converter de Fahrenheit para Celsius
(você deve deduzir a fórmula de Celsius para Fahrenheit):C =
5
(F - 32)
9
"""

unidade = input('Você vai digitar a temperatura em qual escala? ')

if unidade.lower() == 'f':
    f = float(input('Digite a temperatura em Fahrenheit: '))
    c = 5 / 9 * (f - 32)
    print(f'A temperatura digitado equivalente em Celsius é {c:.2f}')
else:
    c = float(input('Digite a temperatura em Celsius: '))
    f = 9 * c / 5 + 32
    print(f'A temperatura digitada equivalente em Fahrenheit é {f:.2f}')

