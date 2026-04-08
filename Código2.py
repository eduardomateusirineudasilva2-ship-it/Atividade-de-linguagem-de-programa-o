preco = float(input("Preço da mercadoira:"))
desconto_porcentagem = int(input("Porcentagem de desconto: % "))

valor_desconto = preco * (desconto_porcentagem / 100)
preco_final = preco - valor_desconto

print(f"preco original; R$ {preco:.2f}" )
print(f"Desconto de: R$ {valor_desconto:.2f}")
print(f"Preço com desconto: R${preco_final:.2f}")
