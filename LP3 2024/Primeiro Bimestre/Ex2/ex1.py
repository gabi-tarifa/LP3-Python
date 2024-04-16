#Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente
#Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
import random

def checarNumeros(num, numSortido):
    if(num == numSortido):
        return "Ganhaste!!"
    elif (num < numSortido):
        return "O número sorteado é maior; escolha outro: "
    else:
        return "O número sorteado é menor; escolha outro: "

numSortido = 1 + (random.choice(range(100)))
print("Escolha um número de 1 a 100: ")

erro = True

while(erro):
    palpite = int(input(""))
    erro = palpite != numSortido
    print(checarNumeros(palpite, numSortido))
