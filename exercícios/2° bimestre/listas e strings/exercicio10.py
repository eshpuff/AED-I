'''Faça um programa em python que receba uma lista de números inteiros como entrada e retorne a maior soma dos números ímpares consecutivos da lista. Caso não haja números ímpares na lista, o programa deve retornar 0.                                        Exemplo de uso da função:                                                                                                             lista = [1, 2, 3, 5, 6, 7, 9, 10]                                                                                                                                Saída esperada:16'''

numeros = []
x = 1
i = 0
impares = []
soma = 0

while x != "0":
    x = input("Insira um número inteiro (Insira 0 para encerrar.): ")
    if x != "0":
        numeros.append(x)
        print("Seus números são:",numeros)

while i < len(numeros):
    if (int(numeros[i])%2) != 0:
        impares.append(numeros[i])
    i += 1

i = 0

while i < len(impares):
    soma += int(impares[i])
    i += 1

print("A soma dos números impares é",soma)
