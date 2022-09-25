print("-- Não compre tinta a mais --")
largura = float(input("Largura da parede em metros: "))
altura = float(input("Altura da parede em metros: "))
area = largura * altura
litros = area / 2

print(f"Dimensão da parede: {largura}x{altura} - Área: {area}m²")
print(f"Você precisará de {litros} litros de tinta.")
