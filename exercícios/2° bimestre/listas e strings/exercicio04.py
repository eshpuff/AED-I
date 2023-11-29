'''Dada uma lista de números inteiros informada pelo usuário, escreva um programa em Python que conte quantos números únicos (diferentes) estão presentes na lista. A digitação dos elementos da lista deve encerrar quando for digitado o número zero.'''

numeros = []
numeros_unicos = []
x = 10
i = 0

while x != "0":
    x = input("Insira um número inteiro (Insira 0 para encerrar.): ")
    if x != "0":
        numeros.append(x)
        print("Seus números são:",numeros)
 
while i < len(numeros):
    if numeros[i] in numeros_unicos:
        numeros_unicos.remove(numeros[i])
    else:
        numeros_unicos.append(numeros[i])
    i += 1

print(numeros_unicos)