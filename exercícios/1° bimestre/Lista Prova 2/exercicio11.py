'''Escreva um programa que mostre a tabuada (0 a 10) de um número fornecido pelo usuário'''

numero = int(input("Insira um número: "))
i = 1
tabuada = numero * i
print ("0")
print(tabuada)

while i < 10:
    i = i + 1
    tabuada = numero * i
    print(tabuada) 