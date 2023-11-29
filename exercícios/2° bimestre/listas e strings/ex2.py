'''Faça uma função que receba, por parâmetro, duas listas contendo números desordenados, que podem estar repetidos. A função deverá retornar uma lista contendo a intersecção entre as listas informadas, sem números repetidos. Exemplo: lista1 = [5,4,3,5,3,4,7,3,1] lista2 = [5,7,3,6,8,7,5,1,3,9] listaResultante = [5,3,7,1]'''
lista1 = []
lista2 = []
lista_resultante = []
x = 1
y = 1
i = 0
z = 0

print("Crie a lista 1:")
while x != "0":
    x = input("Insira um número inteiro (Insira 0 para encerrar.): ")
    if x != "0":
        lista1.append(x)
        print("Lista 1:",lista1)

print("Crie a lista 2:")
while y != "0":
    y = input("Insira um número inteiro (Insira 0 para encerrar.): ")
    if y != "0":
        lista2.append(y)
        print("Lista 2:",lista2)

if len(lista1) > len(lista2):
    while i < len(lista1):
        if lista1[i] in lista_resultante:
            z += 1
        else:
            if lista1[i] in lista2:
                lista_resultante.append(lista1[i])
        i += 1

i = 0
if len(lista2) > len(lista1) or len(lista2) == len(lista1):
    while i <len(lista2):
        if lista2[i] in lista_resultante:
            z += 1
        else:
            if lista2[i] in lista1:
                lista_resultante.append(lista2[i])
        i += 1

print("Lista 1 =",lista1)
print("Lista 2 =",lista2)
print("Lista Resultante =",lista_resultante)

