''' Implementar um programa para multiplicar matrizes. Obs (nro de elementos em cada dimensão): 1ª matriz = (Linhas1 x Colunas1) 2ª matriz = (Linhas2 x Colunas2)'''

def criaMatriz():
    matriz = []
    while True:
        linha = []
        entrada = input("Insira valores para a linha (separados por espaço), ou digite '000' para sair: ")
        valores = entrada.split()
        for valor in valores:
            if valor == "000":
                return matriz
            else:
                linha.append(int(valor))
        matriz.append(linha)

def multiplicaMatrizes(matriz1, matriz2):
    linhas1 = len(matriz1)
    colunas1 = len(matriz1[0])
    linhas2 = len(matriz2)
    colunas2 = len(matriz2[0])

    if colunas1 != linhas2:
        print("Número de colunas na primeira matriz não é igual ao número de linhas na segunda matriz.")
        return None

    resultado = [[0 for _ in range(colunas2)] for _ in range(linhas1)]

    for i in range(linhas1):
        for j in range(colunas2):
            for k in range(linhas2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

print("Matriz 1:")
matriz1 = criaMatriz()
print("Matriz 2:")
matriz2 = criaMatriz()

resultado = multiplicaMatrizes(matriz1, matriz2)
if resultado:
    print("Resultado: ")
    for linha in resultado:
        print(linha)