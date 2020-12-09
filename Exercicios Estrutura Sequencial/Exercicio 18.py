"""
Problema "consumo"
Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
médio do carro, com três casas decimais.
"""

distancia = float(input('Distância total percorrida: '))
combustivel = float(input('Total de combustível gasto: '))

consumo = distancia/combustivel

print(f'O consumo médio é {round(consumo, 3)} km.')
