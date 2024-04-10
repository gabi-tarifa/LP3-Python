#Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente
#Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
import random

numSortido = 1 + (random.choice(range(100)))
palpite = int(input("Escolha um número de 1 a 100: "))

erro = palpite != numSortido

while(erro):
    erro = palpite != numSortido
    if(palpite == numSortido):
        print("Ganhaste!!")
        break
    elif (palpite < numSortido):
        palpite = int(input("O número sorteado é maior; escolha outro: "))
    else:
        palpite = int(input("O número sorteado é menor; escolha outro: "))
    
