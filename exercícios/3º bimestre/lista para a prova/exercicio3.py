'''Faça um programa em Python que crie uma matriz de inteiros de cinco linhas por dez colunas. Leia os valores desta matriz linha após linha, e exiba a matriz na tela coluna por coluna'''

def criaMatriz():
    i = 0
    c = 0
    linha = []
    coluna = []
    while i < 5:
        while c < 10:
            n = int(input("Insira valor para a linha: "))
            linha.append(n)
            c += 1
        print(linha)
        coluna.append(linha)
        linha = []
        c = 0
        i += 1
    return coluna

matriz = criaMatriz()

for i in range(5):
        for j in range(10):
            print(matriz[i][j], end="\t")
        print()


