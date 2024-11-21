periodo = input("Digite M, V ou N para saber o seu turno: ")

if periodo == 'M' or periodo == 'm':
    print(f"Você digitou {periodo} portanto seu turno é Matutino, BOM DIA")

elif periodo == 'V' or periodo == 'v':
    print(f"Você digitou {periodo} portanto seu turno é Vespertino, BOA TARDE")

elif periodo == 'N' or periodo == 'n':
    print(f"Você digitou {periodo} portanto seu turno é Noturno, BOA NOITE")

else:
    print("Turno INVALIDO")


