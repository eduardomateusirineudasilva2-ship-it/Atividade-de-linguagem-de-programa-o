salario = float(input("Salário atual:"))
porcentagem = int(input("Porcentagem de aumento:"))

aumento = salario * (porcentagem/100)
novo_salario = salario + aumento

print(f"Salário antigo: R${salario:.2f}")
print(f"O novo salario é: R${novo_salario:.2f}")