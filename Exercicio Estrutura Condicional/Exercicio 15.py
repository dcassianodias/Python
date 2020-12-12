"""
Problema "troco_verificado"
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma
mercearia. O programa deve ler o preço unitário do produto, a quantidade de unidades compradas
deste produto, e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a
ser devolvido ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem
informando o valor restante conforme exemplo.
"""

preco = float(input('Digite o preço do produto: '))
quantidade = int(input('Digite a quantidade comprada: '))
dinheiro = float(input('Digite o valor pago pelo cliente: '))

if dinheiro >= preco * quantidade:
    troco = dinheiro - preco * quantidade
    print(f'O troco a ser devolvido é {troco}.')
else:
    resto = dinheiro - preco * quantidade
    print(f'Dinheiro insuficiente, faltam {resto:.2f}')


