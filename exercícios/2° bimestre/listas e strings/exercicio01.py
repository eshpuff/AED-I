'''Escreva um programa que leia uma lista de palavras do usuário e retorne outra lista contendo apenas as palavras com mais de 5 caracteres.'''
 
texto = input("Insira um texto: ")

lista = texto.split()
lista_5_caracteres = [] 
i = 0

while i < len(lista):
    if len(lista[i]) > 5:
        lista_5_caracteres.append(lista[i])
    i += 1

print("A(s) palavra(s) com mais de 5 caracteres são:",lista_5_caracteres)