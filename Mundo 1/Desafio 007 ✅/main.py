print("-- Média final --")

notas = (
    float(input("Digite a primeira notas: ")),
    float(input("Digite a seguda notas: ")),
)

result = (notas[0] + notas[1]) / 2
print(f"Nota final (média): {result}")