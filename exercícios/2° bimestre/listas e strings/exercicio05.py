'''Faça um programa em python em que o usuário digite uma lista de números inteiros (até digitar zero). Após, o programa deve mostrar a frequência de cada número na lista, ou seja, quantos números 1 tem, quantos números 2, etc.'''

numeros = []
x = 10
i = 0 
lista = []
frequencia = []

while x != "0":
    x = input("Insira um número inteiro (Insira 0 para encerrar.): ")
    if x != "0":
        numeros.append(x)
        print("Seus números são:",numeros)

while i < len(numeros):
    if numeros[i] in lista:
        posicao = lista.index(numeros[i])
        frequencia[posicao] += 1        
    else:
        lista.append(numeros[i])
        frequencia.append(1)
    i += 1
    
print(lista,frequencia)