compras = ["arroz", "feijao", "carne", 12.2]
print(compras)
print(compras[3])
compras[3] = 99.9
print(compras)
print(len(compras))
print(compras)
print(list(range(5)))

lista = [2.3, 5, 2.1, 7.4, 0]
soma = 0
#somar todos elemntos
for n in lista:
    soma += n
print("\nSoma das notas: ", soma)


#lista posicional
alunos =["Julia", "Julia", "Alguem"]
for n in range(len(alunos)):
    print(f"\nPosicao {n}  da lista: {alunos[n]}")


N = 5
notas = []
for i in range(1, N+1):
    x = int(input("Nota do aluno: "))
    notas.append(x)

media = 0
for n1 in notas:
    media += n1
media = media / N

for n1 in notas:
    if n1 > media:
        print("Aprovados: ", n1)

