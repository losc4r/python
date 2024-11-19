media = float(input("Digite a nota do Lucas: "))

if media >= 6:
    print(f"Lucas tirou {media} e está APROVADO")
elif media <= 4:
    print(f"Lucas tirou {media} e está REPROVADO")
else:
    print(f"Lucas tirou {media} e está em RECUPERAÇÃO")