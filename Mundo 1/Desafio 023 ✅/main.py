print("Unidade, dezena, centena, milhar")
n = int(input("Digite o número: "))

print(f"Unidade: {n % 10}")
print(f"Dezena: {(n//10) % 10}")
print(f"Centena: {(n//100 % 10)}")
print(f"Milhar: {(n//1000) % 10}")
