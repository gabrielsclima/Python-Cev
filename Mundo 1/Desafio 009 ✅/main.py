print("-- Tabuada --")

number = int(input("Número da tabuada: "))
print("_" * 15, "\n")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
print("_" * 15, "\n")