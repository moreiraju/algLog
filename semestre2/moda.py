def calculaModa(numeros, quantidade):
    frequencias = []
    for i in range(quantidade):
        num = numeros[i]
        cont = 0
        for j in range(quantidade):
            if numeros[j] == num:
                cont += 1
        frequencias.append(cont)
    
    maiorFreq = frequencias[0]
    for i in range(quantidade):
        if frequencias[i] > maiorFreq:
            maiorFreq = frequencias[i]

    contMaior = 0
    moda = 0
    for i in range(quantidade):
        if frequencias[i] == maiorFreq:
            contMaior += 1
            moda = numeros[i]

    if contMaior > 1:
        return None
    else:
        return moda


print("Cálculo da Moda de um Vetor:")

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = -1
    while num < 0:
        num = int(input("Digite um número positivo: "))
        if num < 0:
            print("Valor inválido! Digite apenas números positivos.")
    numeros.append(num)

resultado = calculaModa(numeros, quantidade)

if resultado is None:
    print("\nNão existe uma moda.")
else:
    print("\nA moda do vetor é:", resultado)
