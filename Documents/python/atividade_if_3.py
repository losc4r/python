#genero = input("Digite M ou F para descobrir o sexo: ")

#if genero == "M" or genero == 'm':
#    print(f"Você digitou {genero} portanto seu sexo é Masculino")

#elif genero == "F" or genero == 'f':
#    print(f"Você digitou {genero} portanto seu sexo é Feminino") 

#else:
#    print("Sexo inexistente")


#### PODE SER FEITO ASSIM ####

#upper -> converte para caracteres maiúsculos
# lower -> converte para caracteres minúsculos   
    
genero = input("Digite F para Feminino ou M para Masculino: ").lower()
# genero = genero.lower() #
if genero.lower() == "f":
    print("Feminino")
elif genero.lower() == "m":
    print("Masculino")
else:
    print("inválido")