#Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra,
#letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
import random

def fimDeJogo(palSort):
    for letra in palSort:
       fim = letra == "*" or letra == " "
       if not(fim):
           return False
    return True
    

def gerarPalavraOculta(palSort):
    palavraOculta = ""
    for caracter in palSort:
        if caracter != " " and caracter != "-":
            palavraOculta = palavraOculta + "_"
        else:
            palavraOculta = palavraOculta + caracter
    return palavraOculta


def checarLetra(letra, palSort):
    return letra in palSort

palavras = ["ovo", "rabanete", "console", "cozinha", "sala de estar"]
palavraSortida = random.choice(palavras)
tentativas = 11
keepGoing = True
palavraOculta = gerarPalavraOculta(palavraSortida)
palavraManuesada = palavraSortida
while keepGoing:
    print(palavraOculta)
    
    if (fimDeJogo(palavraSortida)):
        print("Ganhaste!!")
        break
    elif tentativas == 0:
        print("Fim de jogo!! A palavra era", palavraSortida)
        break
    
    letra = input("Digite uma letra: ").lower()
        
    if checarLetra(letra, palavraSortida):
        print("Letra certa!!")
        while palavraSortida.find(letra) != -1:
            indice = palavraSortida.find(letra)
            palavraSortida_list = list(palavraSortida)
            palavraSortida_list[indice] = "*"
            palavraOculta_list = list(palavraOculta)
            palavraOculta_list[indice] = letra
            palavraSortida = "".join(palavraSortida_list)
            palavraOculta = "".join(palavraOculta_list)
            
    else:
        tentativas -= 1
        print("Letra errada!")
        print("Tentativas restantes:", tentativas)
        
