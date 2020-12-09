"""
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo)
"""

K = float(input('Digite a velocidade em k/h'))

M = K / 3.6

print(f'A velocidade digitada convertida em m/s é de : {round(M)}')