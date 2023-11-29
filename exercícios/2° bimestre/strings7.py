'''Escreva um programa em python que leia um texto e diga se é ou não um palíndromo (ou seja, se o inverso da string é igual a ela). Não será possível utilizar qualquer função no python que trabalhe com strings.
Exemplos:
Ama
Mirim
A grama é amarga'''

texto = input("Digite um texto: ")
texto_junto = ""


for letra in texto:
    if letra != " ":
        texto_junto += letra

palindromo = 1
i = 0
j = len(texto_junto) - 1

while i < j and palindromo == 1:
    if texto_junto[i] != texto_junto[j]:
        palindromo = 0
    i += 1
    j -= 1


if palindromo == 1:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")