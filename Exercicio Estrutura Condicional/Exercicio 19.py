"""
Problema "aumento"
Uma empresa vai conceder um aumento percentual de salário aos seus funcionários dependendo de quanto
cada pessoa ganha, conforme tabela ao lado. Fazer um programa para ler o salário de uma pessoa, daí mostrar
qual o novo salário desta pessoa depois do aumento, quanto foi o aumento e qual foi a porcentagem de aumento.

Salário atual Aumento
Até R$ 1000.00 20%
Acima de R$ 1000.00 até R$ 3000.00 15%
Acima de R$ 3000.00 até R$ 8000.00 10%
Acima de R$ 8000.00 5%
"""

salario = float(input('Qual o salário do funcionário?: '))

if salario <= 1000.00:
    porcentagem = 20
elif salario < 3000.00:
    porcentagem = 15
elif salario < 8000.00:
    porcentagem = 10
else:
    porcentagem = 5

aumento = salario * porcentagem/100
novo_salario = salario + aumento

print(f'O novo salário do funcionário é {novo_salario:.2f}')
print(f'O aumento foi de {aumento:.2f}')
print(f'A porcentagem de aumento foi de {porcentagem} %')

