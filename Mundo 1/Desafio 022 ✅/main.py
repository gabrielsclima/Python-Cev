print("-- Seu nome de todos os jeitos --")
nome = input("Digite seu nome: ").strip()
separado = nome.split()

print(f"Normal: {nome}")
print(f"Em maiúsculo: {nome.upper()}")
print(f"Em minúsculo: {nome.lower()}")
print(f"Seu nome contém {len(nome) - nome.count(' ')} caracteres")
print(f"Seu primeiro nome contém {len(separado[0])} caracteres")