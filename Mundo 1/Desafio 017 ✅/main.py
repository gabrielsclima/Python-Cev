from math import hypot

print("-- Achar a hipotenusa --")
co = float(input("Medida do cateto oposto: "))
ca = float(input("Medida do cateto adjacente: "))

print(f"A hipotenusa do triângulo retângulo será de {hypot(ca, co):.2f}")