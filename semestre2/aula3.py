"""
Crie um programa que controle vendas e solicite ao usuário: nome do produto, valor, quantidade, 
método de pagamento (1 - a vista, 2 - a prazo), se a prazo solicite nº parcelas e calcule total:
- a vista => desconto de 10%;
- a prazo => acressimo de:
    15% p/até 5 parcelas
    20% acima de 5
Calcule e mostre, total venda, denconto, liquido a pagar;
Se a prazo, mostre valor de cada parcela, e o adicional
"""
nome = input("Digite o nome do produto: ")
valor = float(input("Digite o valor: "))
quantidade = int(input("Qual a quantidade desse produto vc dejesa? "))
pagamento = int(input("Qual método de pagamento vc deseja? Digite 1 para pagar a vista ou 2 para pagar a prazo: "))
if pagamento == 1:
    venda = valor * quantidade
    liquido = 0.9 * venda
    desconto = 0.1 * venda
    print("Valor da venda: ", venda)
    print("Valor líquido da venda: ", liquido)
    print("Valor do desconto: ", desconto)
elif pagamento == 2:
    parcela = int(input("Qual a quantidade de parcelas desejadas: "))
    if parcela <= 5:
        venda = (valor * quantidade) * 1.15
        prazo = venda / parcela
        acressimo = (valor * quantidade) * 0.15
    else:
        venda = (valor * quantidade) * 1.2
        prazo = venda / parcela
        acressimo = (valor * quantidade) * 0.2
    print("Valor da venda: ", venda)
    print("Valor da parcela: ", prazo)
    print("Valor do acréssimo: ", acressimo)
else:
    print("Valor não compreendido.")

