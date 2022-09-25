from random import choice
print("Sorteio de alunos")

# O método a seguir não é recomendado caso seu programa seja utilizado seriamente:
# Ao invés de executar os inputs diretamente na lista/tupla, execute os inputs em variáveis separadas 
# e depois junte-as em uma lista/tupla
alunos = (
    str(input("Primeiro aluno: ")),
    str(input("Segundo aluno: ")),
    str(input("Terceiro aluno: ")),
    str(input("Quarto aluno aluno: ")),
)
escolhido = choice(alunos)
print(f"O aluno escolhido foi: {escolhido}")