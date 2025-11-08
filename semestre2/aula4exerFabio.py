quantidades = []
valores = []
totais = []
totalGeral = 0.0

for i in range(5):
    qtd = int(input("Quantidade: "))
    valor = float(input("Valor: "))
    quantidades.append(qtd)
    valores.append(valor )

    totais.append( (qtd * valor))
    totalGeral += (qtd * valor)

#encontrar produto de maior valor
maior = valores[0] #inicializo maior com um valor qualquer
posicaoMaior = 0
for i in range(len(quantidades)):
    if valores[i] > maior:
        maior = valores[i]
        posicaoMaior = i

print(quantidades)
print(valores)
print(totais)
print("Total Estoque: ", totalGeral)
print("Qtd produto maior Valor: ", quantidades[posicaoMaior])