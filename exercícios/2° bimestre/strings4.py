'''Escreva um programa que recebe uma string do usuário e imprime a string com todas as letras maiúsculas convertidas para minúsculas e vice-versa.'''

string = input("Insira um texto: ")
i = 0
frase = ""

while i < len(string):
    if ord(string[i]) <= 90 and ord(string[i]) > 64:
        frase = frase + chr(ord(string[i]) + 32)
    else:
        frase = frase + chr(ord(string[i]) - 32)
    i += 1
                            
print(frase)