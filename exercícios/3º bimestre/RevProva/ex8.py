'''8) Faça um programa em Python que leia três listas compostas por cinco números fornecidos
pelo usuário. Crie uma matriz que reúna estas três listas (as listas podem ser as linhas ou as
colunas da matriz). Apresente o conteúdo da matriz, assim como o seu maior valor contido.'''

def inputs():
    list1 = []
    list2 = []
    list3 = []

    for i in range(5):
        value1 = int(input(f"Insira o {i + 1}º número (primeira lista): "))
        list1.append(value1)

    for i in range(5):
        value2 = int(input(f"Insira o {i + 1}º número (segunda lista): "))
        list2.append(value2)

    for i in range(5):
        value3 = int(input(f"Insira o {i + 1}º número (terceira lista): "))
        list3.append(value3)

    return list1, list2, list3

def creating():
    lista1, lista2, lista3 = inputs()
    matriz = [lista1, lista2, lista3]
    return matriz

def finding(matriz):
    maior_valor = matriz[0][0]
    for linha in matriz:
        for numero in linha:
            if numero > maior_valor:
                maior_valor = numero
    return maior_valor

matriz = creating()
maior_valor = finding(matriz)

def format(matriz):

    for linha in matriz:
        print("|", end=" ")  # barra no inicio
        for numero in linha:
            print(numero, end=" ")
        print("|")  # barra no final da linha

format(matriz)
print(f"O maior valor na matriz é: {maior_valor}")
