print("-- Maior e menor --")
numbers = [
    float(input("Primeiro número: ")),
    float(input("Segundo número: ")),
    float(input("Terceiro número: ")),
]

numbers.sort()
print()
print(f"Maior número: {numbers[2]}")
print(f"Menor número: {numbers[0]}")
