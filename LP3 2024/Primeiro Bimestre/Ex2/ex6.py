# Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100),
# converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

def converterNota(nota):
    if (nota > 10 and nota < 0.0):
        print("Não existe nota maior que 10 ou menor que 0")
    elif (nota >= 9.7):
        return "A+"
    elif (nota >= 9.3):
        return "A-"
    elif (nota >= 9.0):
        return "A"
    elif (nota >= 8.7):
        return "B+"
    elif (nota >= 8.3):
        return "B-"
    elif (nota >= 8.0):
        return "B"
    elif (nota >= 7.7):
        return "C+"
    elif (nota >= 7.3):
        return "C-"
    elif (nota >= 7.0):
        return "C"
    elif (nota >= 6.7):
        return "D+"
    elif (nota >= 6.3):
        return "D-"
    elif (nota >= 6.0):
        return "D"
    else:
        return "F"
    
nota = float(input("Digite sua nota de 0.0 a 10.0: "))
if (nota <= 10 and nota >= 0.0):
    print("Sua nota no sistema americano seria", converterNota(nota))
else:
    print("Nota inexistente inserida")
