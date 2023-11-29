'''Faça um programa em Python que leia três listas compostas por cinco números fornecidos pelo usuário. Crie uma matriz que reúna estas três listas (as listas podem ser as linhas ou as colunas da matriz). Apresente o conteúdo da matriz, assim como o seu maior valor contido.'''


def criaLista():
    lista = []
    i = 0
    while i < 5:
        x = int(input("Insira valor: "))
        lista.append(x)
        print(lista)
        i +=1
    return lista
    
def criaMatriz(lista1,lista2,lista3):
    matriz = []
    matriz.append(lista1)
    matriz.append(lista2)
    matriz.append(lista3)
    return matriz

i = 0

lista1 = criaLista()


lista2 = criaLista()


lista3 = criaLista()

matriz = criaMatriz(lista1, lista2, lista3)

print(matriz)