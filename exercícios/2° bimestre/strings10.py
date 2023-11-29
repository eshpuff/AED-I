'''Faça um programa em python que leia três textos. O programa deve imprimir o primeiro texto substituindo todas as ocorrências do segundo pelo terceiro. Não deve ser utilizada qualquer função no python que trabalhe com strings.'''

texto1 = input("Insira o primeiro texto: ")
texto2 = input("Insira o segundo texto: ")
texto3 = input("Insira o terceiro texto: ")

length1 = len(texto1)
length2 = len(texto2)
length3 = len(texto3)

resultado = ""

i = 0
while i < length1:
    if i <= length1 - length2 and texto1[i:i+length2] == texto2:
        resultado += texto3
        i += length2
    else:
        resultado += texto1[i]
        i += 1

print(resultado)
