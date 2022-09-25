print("-- Voe -- ")
distancia = float(input("Distância da viagem em km: "))

if distancia <= 200:
    price = 0.50 * distancia
    print(f"O preço da viagem será de R${price:.2f}")

else:
    price = 0.45 * distancia
    print(f"O preço da viagem será de R${price:.2f}")