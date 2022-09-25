print("-- Conversor de Real(R$) para Dólar($) --")
print("($) = R$ 5,26 (atualizado 24/09/2022)\n")

compra = float(input("Quanto você quer trocar? R$"))
convert = compra * 0.19
print(f"Você poderá comprar ${convert:.2f}\nObrigado!")