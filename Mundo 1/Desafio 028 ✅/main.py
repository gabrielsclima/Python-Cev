from time import sleep
from random import randint
print("-- Jogo da adivinhação --")

print("Pensando em um número de 0 a 5...")
sleep(3)
number = randint(0, 5)
resposta = int(input("Tente adivinhá-lo: "))

if number == resposta:
    print("Parabéns, você acertou!")

else:
    print("Você errou... que pena.")