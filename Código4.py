dias = int(input("Dias que o carro foi alugado: "))
km_percorridos = int(input("KM percorridos: "))


preco_dia = dias * 60
preco_km = km_percorridos * 0.15
total = preco_dia + preco_km

print(f"O total a pagar é de R$ {total:.2f}")