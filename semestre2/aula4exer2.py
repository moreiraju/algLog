valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
print(valores)

v1 = valores[1:4]
print(v1)

print(valores[3:])

print(valores[:3])

print(valores[1:7:2])


x= [5, 7, 8]
n1 = x[0]
n2 = x[1]
n3 = x[2]

print("n1: ", n1)

#unpacking
[a, b, c] = x
print(a)
print(b)


a = [1, 2, 3]
b = [4, 5, 6]
#concatenando a e b em uma só lista
lista = a+b
print(lista)

listaATripla = a * 3
print(listaATripla)


print(a)
b = a #b não recebe uma cópia de a, mas faz uma referência (apontar) ao endereço de a
b = a[:] #agora b recebeu a cópia de a
print(b)
a.append(-5)
print(a)
print(b)


a.reverse() #inverte a lista
a.sort() #ordena
print(a)