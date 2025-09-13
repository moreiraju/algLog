""""
EXEMPLO DE UTILIZAÇÃO DO WHILE
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

soma = 0
while a <= b:
    print(a)
    a = a + 1
    soma = soma + a
print("Fim do programa")
media = soma / b
print(media)
"""

#Com while, crie um algoritmo para calcular a média de N números

n = int(input("Digite a quantidade de números desejado: "))
i = 0
soma = 0
while  i < n:
    numero = int(input("Digite o número: "))
    soma = soma + numero
    i = i + 1
media = soma/n
print(f"{media} \nFIM DO PROGRAMA")


#Percorre todo array com for
lista = [10, 5, -10, -50]
for n in [10, 15, 20, 30, -1, 40]:
    print(n)
print("FIM DO PROGRAMA\n")

soma = 0
for y in lista:
    print(y)
    soma += y 
print("Soma da lista: ", soma, "FIM DO PROGRAMA\n\n")


produtos = ["maça", "banana", "laranja", "cenoura", "morango"]
for p in produtos:
    print(p)
print("FIM DO PROGRAMA\n\n")


#range, gera valor de n à n, ex: range(10), range(3, 20)...
for n in range(10):
    print("Valor = ", n)
