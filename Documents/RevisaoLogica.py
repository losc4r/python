# criação da variável nome do aluno
nome_aluno = ""
# criação de variáveis para obter as quatro notas
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
nota4 = 0.0

# vamos obter o nome do aluno
nome_aluno = input("Digite o nome do aluno: ")

# vamos obter as notas dos alunos
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# somar as 4 notas, obter a média e a situação
# >= 7 Aprovado | <= 4 Reprovado | >4 e <7 Recuperação
# o f após o print é para mostrar o valor da conta 
media = (nota1+nota2+nota3+nota4) / 4
if media>=7:
    print(f"A média é {media} - Aprovado")
elif media<=4:
    print(f"A média é {media} - Reprovado")
else: 
    print(f"A média é {media} - Recuperação")

