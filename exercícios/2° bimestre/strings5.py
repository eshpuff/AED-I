''' Escreva um programa que recebe uma frase do usuário e conta o número de palavras na frase.'''

frase = input("Insira uma frase: ")
palavras = 1

for i in frase:
    if i == " ":
        palavras += 1

print("O número de palavras nessa frase é:", palavras)
