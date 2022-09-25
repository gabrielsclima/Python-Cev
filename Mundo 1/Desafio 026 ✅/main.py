print("Primeira e última ocorrência de uma str")
frase = input("Digite algo: ").upper().strip()

print("Quantidade de \"A's\":", frase.count("A"))
print("Posição do primeiro \"A\":", frase.find("A"))
print("Posição do último \"A\":", frase.rfind("A"))
