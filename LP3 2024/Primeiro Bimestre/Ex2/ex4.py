#Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos.
#O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi o vencedor.
def contarVotos():
    if(votos1 > votos2 and votos1 > votos3):
        return "O vencedor é: Candidato 1!!"
    elif(votos2 > votos1 and votos2 > votos3):
        return ("O vencedor é: Candidato 2!!")
    elif(votos3 > votos1 and votos3 > votos2):
        return ("O vencedor é: Candidato 3!!")
    else:
        return("Houve um empate!")

votos1 = 0
votos2 = 0
votos3 = 0
voto = int(input("Escolha um dos três candidatos para votar (escolha um número):\nCandidato 1;\nCandidato 2;\nCandidato 3;\n"))

while(voto == 1 or voto == 2 or voto == 3):
    if (voto == 1):
        votos1 = votos1 + 1
    elif (voto == 2):
        votos2 = votos2 + 1
    else:
        votos3 = votos3 + 1

    voto = int(input("Escolha um dos três candidatos para votar (escolha um número):\nCandidato 1;\nCandidato 2;\nCandidato 3;\n"))

print("Fim da votação!!")
print(contarVotos())
