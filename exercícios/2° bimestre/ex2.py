'''Leia uma palavra e tente transformar de  maiusculo para minusculo'''

palavra = input("Insira uma palavra usando letras maíusculas: ")
i = 0
minusculo = ""

while i < len(palavra):
    minusculo = minusculo + chr(ord(palavra[i]) + 32)
    i += 1
    
print(minusculo)
