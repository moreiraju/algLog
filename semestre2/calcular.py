def calcular(a, b, operacao):
    if operacao == "somar":
        return a + b
    elif operacao == "subtrair":
        return a - b
    elif operacao == "multiplicar":
        return a * b
    elif operacao == "dividir":
        return a / b
    else:
        return "Operação inválida!"


o = input("Digite a operação: ").strip() #strip remove espaco antes e depois
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("\nResultados:")
print("Soma:", calcular(a, b, "somar"))
print("Subtração:", calcular(a, b, "subtrair"))
print("Multiplicação:", calcular(a, b, "multiplicar"))
print("Divisão:", calcular(a, b, "dividir"))
