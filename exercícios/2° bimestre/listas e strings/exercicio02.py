'''Escreva um programa que receba uma lista de números e retorne uma nova lista contendo apenas os números pares.'''

numeros = input("Insira números: ")
list_numeros = numeros.split()
pares = []
i = 0


while i < len(list_numeros):
    if (int(list_numeros[i])%2) == 0:
        pares.append(list_numeros[i])
    i += 1

print(pares)



