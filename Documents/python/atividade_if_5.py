n1 = int (input("Digite um número: "))
n2 = int (input("Digite outro número: "))
n3 = int (input("Digite mais um número: "))

if n1 > n2 and n1 > n3: 
    print(f"O número {n1} é o maior entre os que você digitou")
elif n2 > n1 and n2 > n3: 
    print(f"O número {n2} é o maior entre os que você digitou")
else:
    print(f"O número {n3} é o maior entre os que você digitou")