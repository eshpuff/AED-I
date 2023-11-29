''' Faça um programa em python que leia uma frase e a passe para maiúscula.'''

palavra = input("Insira uma palavra usando letras minusculas: ")
i = 0
maiuscula = ""

while i < len(palavra):
    maiuscula = maiuscula + chr(ord(palavra[i]) - 32)
    i += 1
    
print(maiuscula)