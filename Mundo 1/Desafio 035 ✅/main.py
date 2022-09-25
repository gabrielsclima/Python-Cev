print("-- Formação de triângulo --")

a = float(input("Primeira reta: ")),
b = float(input("Segunda reta: ")),
c = float(input("Terceira reta: ")),

if a+b > c and b+c > a and a+c > b:
    print("As retas podem formar um triângulo!")

else:
    print("As retas não podem formar um triângulo.")
