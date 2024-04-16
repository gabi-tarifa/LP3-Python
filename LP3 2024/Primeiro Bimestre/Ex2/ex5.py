#Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo

def palavraInversa(palavra):
    palInversa = ""
    for letra in palavra[::-1]:
        palInversa = palInversa + letra
    return palInversa.lower()


palavra = input("Escreva uma palavra e nós diremos se é palíndromo ou não: ")
palavra = palavra.lower()
if (palavra == palavraInversa(palavra)):
    print("É um palíndromo.")
else:
    print("Não é palíndromo")
