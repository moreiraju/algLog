n1 = int(input("Digite o valor 1: "))
n2 = int(input("Digite o valor 2: "))

while n1 <= n2:
    print(n1)
    n1 = n1 + 1


valores = [5, 20, 16, 18, 55, 59]
for x in valores:
    print(x)

nomes = ['joao', 'julia', 'marcio']
for nome in nomes:
    print(nome)


n = int(input("Digite o número desejado: "))
i = 0
while  i <= 10:
    print(f'{n}  x  {i} = {n*i}')
    i = i+1
