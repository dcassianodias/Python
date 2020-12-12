"""
Problema "notas"
Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal)
no ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 6.00, mostrar
a mensagem "REPROVADO".
"""

nota1 = float(input('Digite a nota do primeiro semestre: '))
nota2 = float(input('Digite a nota do segundo semestre: '))

nota_final = nota1 + nota2

if nota_final < 6.00:
    print(f'Sua nota final foi: {nota_final:.1f}. Aluno reprovado.')
else:
    print(f'Sua nota final foi: {nota_final:.1f}. Parabéns você foi aprovado!!!!!')
