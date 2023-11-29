'''Leia uma palavra e diga se essa palavra é palíndromo'''

palavra = input("Digite uma palavra: ")
palavra = palavra.lower()

if palavra == palavra[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")

