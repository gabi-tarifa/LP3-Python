# Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.
def vogaisConsoantes(frase):
    consoantes = 0
    vogais = 0
    for letras in frase:
        if (letras == "a" or letras == "A" or letras == "e" or letras == "E" or letras == "i" or letras == "I" or letras == "o" or letras == "O" or letras == "u" or letras == "U"):
            vogais = vogais + 1
        else:
            consoantes = consoantes + 1

    return "Consoantes:", consoantes, "\nVogais: ",vogais

frase = input("Digite uma frase(sem acentuação): ")
print(vogaisConsoantes(frase))
