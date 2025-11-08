def calculaDesconto(valorCompra, idade):
    descontoBase = 0.0
    if valorCompra > 500:
        descontoBase = 0.15
    elif valorCompra > 200:
        descontoBase = 0.10


    descontoAdicional = 0.0
    if idade < 25:
        descontoAdicional = 0.05
    elif idade >= 60:
        descontoAdicional = 0.07


    valorDescontoBase = valorCompra * descontoBase
    valorDescontoAdicional = valorCompra * descontoAdicional


    valorFinal = valorCompra - (valorDescontoBase + valorDescontoAdicional)


    return valorDescontoBase, valorDescontoAdicional, valorFinal



print("Cálculo de Desconto - Loja Online")

idade = int(input("Informe sua idade: "))
valorCompra = float(input("Informe o valor total da compra: "))

descontoBase, descontoAdicional, valorFinal = calculaDesconto(valorCompra, idade)


print("\nResultado:")
print(f"Valor do desconto base: R$ {descontoBase:.2f}")
print(f"Valor do desconto adicional: R$ {descontoAdicional:.2f}")
print(f"Valor final a ser pago: R$ {valorFinal:.2f}")
