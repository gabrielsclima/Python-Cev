print('-- Radar --')
velocidade = float(input("Velocidade em km/h: "))

if velocidade > 80:
    print("Limite de 80km/h excedido!")
    print(f"Multado em R${(velocidade - 80) * 7}")

else:
    print("Pass")

print("Dirija com segurança")