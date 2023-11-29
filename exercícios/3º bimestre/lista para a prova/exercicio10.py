'''Escreva um programa em Python que calcule o comprimento da mais longa sequência de espaços em branco em uma string lida.'''

string = input("Insira um texto: ")
espaços = 0
maiorSequencia = 0

for caracter in string:
    if caracter ==  " ":
        espaços += 1
        if espaços > maiorSequencia:
            maiorSequencia = espaços
    else:
        espaços = 0

print("A maior sequência de espaços em branco é:", maiorSequencia)