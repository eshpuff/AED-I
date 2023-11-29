'''Escreva um programa que receba duas listas do usuário e retorne uma nova lista contendo apenas os elementos comuns entre as duas listas.'''

texto1 = input("Insira a primeira lista: ")
lista_1 = texto1.split()
texto2 = input("Insira a segunda lista: ")
lista_2 = texto2.split()
i = 0
lista_final = []

if len(lista_1) > len(lista_2):
    while i < len(lista_1):
        if lista_1[i] in lista_2:
            lista_final.append(lista_1[i])
        i += 1

i = 0

if len(lista_2) > len(lista_1):
    while i < len(lista_2):
        if lista_2[i] in lista_1:
            lista_final.append(lista_2[i])
        i += 1

elif len(lista_1) == len(lista_2):
    while i < len(lista_2):
        if lista_2[i] in lista_1:
            lista_final.append(lista_2[i])
        i += 1
        
print(lista_final)