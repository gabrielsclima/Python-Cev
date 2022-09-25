print("=== Mercado do Zé ===")

preço = float(input("Digite o preço do produto: R$"))
desconto = preço - (preço / 100 * 5)
print(f"Desconto de 5%: R${desconto}")
print("Até mais!")