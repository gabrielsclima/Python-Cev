print("-- Aluguel de carros --")
dias = int(input("Dias de utilização do carro: "))
km = float(input("Quantos KM rodados: "))

total = (60 * dias) + (0.15 * km)

print(f"Total a ser pago: R${total}")