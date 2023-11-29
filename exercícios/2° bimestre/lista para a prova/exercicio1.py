'''Crie uma lista com números aleatórios (pelo menos 5 elementos) e crie um menu interativo que permita ao usuário escolher as seguintes opções: Ver a lista completa; Ver a soma dos elementos da lista; Ver o maior número da lista; Ver o menor número da lista'''

import random

lista = []
maior = 0
soma = 0
numero_anterior = 0
i = 0
cont = 0
menor = 0
while len(lista) < 5:
    x = random.randint(0,100)
    lista.append(x)

menu = input("Se você quer ver a lista insira 1.\n Se você quer ver a soma dos elementos insira 2.\n Se você quer ver o maior número da lista insira 3.\n Se você quer ver o menor número da lista insira 4.\n Se deseja sair insira 0: ")

while menu != "0":
    if menu == "1":
        print("A lista é:",lista)
    if menu == "2":
        for i in lista:
            soma += i
        print("A soma dos elementos da lista é",soma)
    if menu == "3":
        while i < len(lista):
            if int(lista[cont]) > numero_anterior:
                maior = int(lista[cont])
                numero_anterior = int(lista[cont])
            i += 1
            cont += 1
        print("O maior número da lista é",maior)
    i = 0
    cont = 0
    numero_anterior = 101
    if menu == "4":
        while i < len(lista):
            if int(lista[cont]) < numero_anterior:
                menor = int(lista[cont])
                numero_anterior = int(lista[cont])
            i += 1
            cont += 1
        print("O menor número da lista é",menor)   
    menu = input("Se você quer ver a lista insira 1.\n Se você quer ver a soma dos elementos insira 2.\n Se você quer ver o maior número da lista insira 3.\n Se você quer ver o menor número da lista insira 4.\n Se deseja sair insira 0: ")

if menu == "0":
    print("Tchau é nós.")