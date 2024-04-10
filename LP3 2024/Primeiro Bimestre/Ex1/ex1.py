#ex 1

numero_ex1 = int(input("Insira um número inteiro: "))
print("O antecessor é ", numero_ex1 - 1, " e o sucessor é", numero_ex1 + 1, ".")

#ex 2

numero1_ex2 = float(input("Insira três números(Insira um número e aperte enter): "))
numero2_ex2 = float(input(""))
numero3_ex2 = float(input(""))

print("A media dos três números é: ", (numero1_ex2 + numero3_ex2 + numero2_ex2)/3)

#ex 3

valor_ex3 = float(input("Insira o preço da sua compra(Somente valor numérico): "))

if valor_ex3<10:
    desconto = int(0)
elif valor_ex3<100:
    desconto = int(5)
elif valor_ex3<500:
    desconto = int(10)
else:
    desconto = int(15)

novoValor = valor_ex3 - (valor_ex3 * (desconto/100))

print("A compra de R$", valor_ex3, ", com desconto de ", desconto, "%, agora possui um valor de R$", novoValor, "com valor descontado de R$", valor_ex3 - novoValor)
