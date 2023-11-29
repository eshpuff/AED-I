'''1) Faça um programa em Python para ler “n” números inteiros, armazenando-os em uma
lista (o usuário informará um valor inteiro positivo para “n”). Após, crie duas outras listas a
partir desta primeira digitada, sendo que uma conterá os números positivos (>= 0), e a outra
conterá os números negativos. Mostre na tela como ficaram as três listas'''

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

    for numeros in listaNumeros:
        if numeros >= 0:
            listaPositivos.append(numeros)

        else:
            listaNegativos.append(numeros)

print("Lista de números:", "\n" , listaNumeros)
print("Lista de positivos:", "\n" , listaPositivos)
print("Lista de negativos:", "\n" , listaNegativos)
