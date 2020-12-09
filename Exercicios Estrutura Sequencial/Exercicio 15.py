"""
Problema "troco"
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma
mercearia. O programa deve ler o preço unitário do produto, a quantidade de unidades compradas
deste produto, e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu
programa deve mostrar o valor do troco a ser devolvido ao cliente.
"""

preco = float(input('Qual o preço do produto?: '))
quantidade = int(input('Quantos produtos o cliente está comprando?: '))
dinheiro = float(input('Qual o valor recebido pelo cliente?: '))

custo = quantidade * preco
troco = dinheiro - (quantidade * preco)

print(f"O cliente comprou {quantidade} produto(s),que custaram {round(custo, 2)} reais, pagou {round(dinheiro, 2)} reais"
      f" e recebeu {round(troco, 2)} reais de troco.")
