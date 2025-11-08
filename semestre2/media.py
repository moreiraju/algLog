def calcularMedia(numeros):
    """soma = 0
    cont = 0
    for n in numero:
        soma = soma + n
        cont = cont + 1"""
    return sum(numeros) / len(numeros)

def mediaPonderada(numeros, pesos):
    soma = 0
    for n in range(len(numeros)):
        soma += numeros[n] * pesos[n]
    return soma/sum(pesos)

lista = [2, 4, 5, 7, 8]
pesos = [1, 2, 3, 1, 3]
print("Tamanho: ", len(lista))

media = calcularMedia(lista)
print("média: ", media)

mediaP = mediaPonderada(lista, pesos)
