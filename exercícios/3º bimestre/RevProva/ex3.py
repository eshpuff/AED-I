'''3) Faça um programa em Python que crie uma matriz de inteiros de cinco linhas por dez
colunas. Leia os valores desta matriz linha após linha, e exiba a matriz na tela coluna por
coluna.
'''

matriz = [[0 for coluna in range(10)] for linha in range(5)]

for coluna in range(5):
    for linha in range(10):
        valor = int(input(f"Digite o valor da posição [{linha+1}][{coluna+1}]: "))
        matriz[coluna][linha] = valor

print("matrizona zica:")

for coluna in range(5):
    for linha in range(10):
        print(matriz[coluna][linha], end="\t")
    print()