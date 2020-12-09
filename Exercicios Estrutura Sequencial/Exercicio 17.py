"""
Problema "pagamento"
Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário
com uma mensagem explicativa, conforme exemplo.
"""

nome = input('Digite o nome do funcionário: ')
valor_hora = float(input('Informe o valor recebido por hora: '))
horas_trabalhadas = int(input('Digite o total de horas trabalhadas: '))

pagamento = valor_hora * horas_trabalhadas

print(f'O pagamento para {nome} deve ser {round(pagamento, 2)}')
