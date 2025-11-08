def contarVogais(texto):
    vogais = "aeiou"
    cont = 0

    for c in texto:
        for v in vogais:
            if c == v:
                cont += 1
    return cont

texto = input("Digite texto: ")
print(contarVogais(texto))
contarVogais(texto)