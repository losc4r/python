genero = input("Digite M ou F para descobrir o sexo: ")

if genero == "M" or genero == 'm':
    print(f"Você digitou {genero} portanto seu sexo é Masculino")

elif genero == "F" or genero == 'f':
    print(f"Você digitou {genero} portanto seu sexo é Feminino") 

else:
    print("Sexo inexistente")