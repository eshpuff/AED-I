'''Escreva um programa que recebe uma string do usuário e imprime a string invertida.'''

palavra = input("Insira uma palavra: ")
i = 0
invertida = ""

for i in palavra:
    invertida = palavra[::-1]
    

print(invertida)