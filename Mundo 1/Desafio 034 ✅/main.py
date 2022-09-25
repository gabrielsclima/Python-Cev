print("-- Aumento de salário --")
salário = float(input("Salário atual: "))

if salário > 1250:
    aumento = salário + ((salário/100) * 10)
    print(f"Total com o aumento: R${aumento:.2f}")

else:
    aumento = salário + ((salário/100) * 15)
    print(f"Total com o aumento: R${aumento:.2f}")