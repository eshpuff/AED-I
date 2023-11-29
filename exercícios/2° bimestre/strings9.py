'''Escreva um programa em python que leia uma string, e substitua cada segmento de dois ou mais espaços em branco por um só caractere de espaço. Não deve ser utilizada qualquer função no python que trabalhe com strings.'''

texto = input("Insira um texto: ")

final = ""
espaco = 0

i = 0
while i < len(texto):
    if texto[i] == " ":
        if espaco == 0:
            final += texto[i]
            espaco = 1
    else:
        final += texto[i]
        espaco = 0

    i += 1

print(final)

