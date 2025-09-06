
"""
ENTENDENDO AS ESTRUTURAS: 

x = int(input("Digite um número: "))

# Em python o código deve ser idento
if x > 0:
    print("Positivo")
print("FIM DO PROGRAMA")

y = int(input("Digite um valor inteiro: "))
if x % 2 == 0:
    print("O valor ", y, " é par")
print("Fim do programa")
"""
# APLICANDO:

nota = int(input("Digite a nota de um aluno: "))
if nota >= 30 and nota < 60:
    print("O aluno está de sub com a nota: ", nota)
print("FIM DO PROGRAMA")


x = int(input("Digite um número: "))

#Verifica se é par ou ímpar
if x % 2 == 0:
    print("O valor ", x, " é par.")
else:
    print("O valor ", x, " é ímpar.")
print("Fim do programa")

#Verifica se é zero, positivo ou negativo
if x == 0:
    print("O valor ", x, " é igual a zero.")
else:
    if x > 0:
        print("O valor ", x, " é positivo.")
    else:
        print("O valor ", x, " é negativo.")
print("Fim do programa")

