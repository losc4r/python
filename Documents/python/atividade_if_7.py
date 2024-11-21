salario = float(input("Digite o salário do funcionário e tecle Enter: "))

if salario <= 280:
    valor_aumento = salario * 20.0 / 100
    novo_salario = salario + valor_aumento
    print(f"O salário antigo é {salario} e foi reajustado em 20%. E o valor de aumento é {valor_aumento} e o novo salário é de {novo_salario}")

elif salario <= 700 :
    valor_aumento = salario * 15.0 / 100
    novo_salario = salario + valor_aumento
    print(f"O salário antigo é {salario} e foi reajustado em 15%. E o valor de aumento é {valor_aumento} e o novo salário é de {novo_salario}")

elif salario <= 1500 :
    valor_aumento = salario * 10.0 / 100
    novo_salario = salario + valor_aumento
    print(f"O salário antigo é {salario} e foi reajustado em 10%. E o valor de aumento é {valor_aumento} e o novo salário é de {novo_salario}")

else:
    valor_aumento = salario * 5.0 / 100
    novo_salario = salario + valor_aumento
    print(f"O salário antigo é {salario} e foi reajustado em 5%. E o valor de aumento é {valor_aumento} e o novo salário é de {novo_salario}")