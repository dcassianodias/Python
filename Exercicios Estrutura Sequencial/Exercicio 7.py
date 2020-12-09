"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
"""

F = float(input('Digite a temperatura em Fahrenheit: '))

C = 5.0 * (F - 32.0)/ 9.0

print(f'A temperatura digitada convertida em Celsius é: {round(C)}')