def imprimeCompras():
    compras = ["Miojo"]
    print("Lista de compras")
    for item in compras:
        print("Produto: ", item)
# fim da funcao

print("Antes da função")

imprimeCompras()
print("Depois da função")

def reajuste(salario, juros = 0.25):
    return salario + salario * juros

print("Reajuste 1: ", reajuste(100))
print("reajuste 2: ", reajuste(100, 0.10))

def maior(x,y):
    if x > y:
        return x
    else:
        return y
        print("Essa mensagem não será impressa:");

#fim da funcao

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
z = maior(x, y)
print("O maior valor é :", z)