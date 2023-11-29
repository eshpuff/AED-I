'''Faça um programa em python que leia uma frase e passe para maiúscula a primeira letra de cada palavra. Você não deve utilizar as 
funções prontas do python para converter para maiúscula ou minúscula.'''

frase = input("Insira uma frase: ")
minusculo = ""
frase_final = ""
i = 0
cont = 0

while i < len(frase):
    if ord(frase[i]) <= 90 and ord(frase[i]) > 64:
        minusculo = minusculo + chr(ord(frase[i]) + 32)
    else:
        minusculo = minusculo + frase[i]
    i += 1

while cont < len(minusculo):
    if cont == 0  or minusculo[cont - 1] == " ":
        frase_final = frase_final + chr(ord(minusculo[cont]) - 32)

    else:
        frase_final = frase_final + minusculo[cont]
    cont += 1

print(frase_final)