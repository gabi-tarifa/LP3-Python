# Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.
def tabuada(num):
    for i in range(10):
        print(num * (i+1))


num = int(input("Digite um número: "))
tabuada(num)

