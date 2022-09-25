from random import shuffle
print("Ordem de apresentação")

alunos = [
    str(input("Primeiro aluno: ")),
    str(input("Segundo aluno: ")),
    str(input("Terceiro aluno: ")),
    str(input("Quarto aluno: ")),
]

shuffle(alunos)
print("Ordem de apresentação: ")
for i in range(4):
    print(f"{1+i}º: {alunos[i]}")

# Desculpem-me. Não consigo me segurar quando sei que posso deixar mais compacto (risos).