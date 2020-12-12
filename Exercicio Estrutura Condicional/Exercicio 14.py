"""
Problema "operadora"
Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.
"""

minutos = int(input('Digite a quantidade de minutos: '))

valor = 50.0

if minutos > 100:
    valor = valor + 2 * (minutos - 100)
    print(f'O valor a pagar é: {valor:.2f}')

