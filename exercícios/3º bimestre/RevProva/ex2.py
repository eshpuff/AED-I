'''2) Baseado no programa anterior, remova todas as ocorrências do valor zero na lista dos
números positivos. Mostre na tela as três listas, informando a quantidade de zeros que
havia, o total de números remanescentes na lista de positivos e na de negativos.'''

listaNumeros = []
num = ''

while num != ' ':
    num = input('Digite quantos números você quiser e pressione enter se quiser parar: ')

    if num == '':
        listaNumeros[:-1]
        break

    num = int(num)
    listaNumeros.append(num)

listaPositivos = []
listaNegativos = []
cont = 0

for numeros in listaNumeros:
    if numeros > 0:
        listaPositivos.append(numeros)
    elif numeros < 0:
        listaNegativos.append(numeros)
    else:
        cont += 1

print("Quantidade de zeros:", cont)
print("Lista de números:", "\n" , listaNumeros)
print("Lista de positivos:", "\n" , listaPositivos)
print("Lista de negativos:", "\n" , listaNegativos)
