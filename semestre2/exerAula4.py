"""
Solicite ao usuário informar a quantidade e o valor de 5 produtos, e:
a) mostre a qtd, valor e total 
b) qual a qtd do produto de maior valor
c) calcule a soma do total de cada produto
"""

N = 5
produtos = []


for i in range(1, N + 1):
    quantidade = int(input("Quantidade do produto: "))
    valor = float(input("Valor do produto: "))
    total = quantidade * valor
    produtos.append({"quantidade": quantidade, "valor": valor, "total": total})


maiorValor = produtos[0]["valor"]
posicao = 0


for i in range(N):
    print(f"\nPRODUTO {i + 1}")
    print(f"Quantidade: {produtos[i]['quantidade']}, Valor: {produtos[i]['valor']}, Total: {produtos[i]['total']}")
    
    if produtos[i]["valor"] > maiorValor:
        maiorValor = produtos[i]["valor"]
        posicao = i


print(f"\nA quantidade do produto de maior valor é {produtos[posicao]['quantidade']}")


soma_total = 0
for i in range(N):
    soma_total += produtos[i]["total"]

print(f"Soma do total de todos os produtos: {soma_total}")
