''' Implementar um programa para somar matrizes. Obs.: as matrizes obrigatoriamente têm a mesma dimensão.'''

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

def somaMatrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("As matrizes precisam ter o mesmo tamanho.")
        return None
    
    resultado = []
    for i in range(len(matriz1)):
        linha_resultado = []
        for j in range(len(matriz1[0])):
            soma_elementos = matriz1[i][j] + matriz2[i][j]
            linha_resultado.append(soma_elementos)
        resultado.append(linha_resultado)
    return resultado

print("Crie a primeira matriz:")
matriz1 = criaMatriz()
print(matriz1)
print("Crie a segunda matriz: ")
matriz2 = criaMatriz()
print(matriz2)

resultado = somaMatrizes(matriz1, matriz2)

if resultado:
    print("Resultado:")
    for linha in resultado:
        print(linha)
