'''Implemente uma função em Python que verifica se a soma dos valores contidos na diagonal principal de uma matriz informada por parâmetro é maior ou igual a soma dos valores da sua diagonal secundária. Por exemplo:M = [[1,2,3], [2,3,4], [4,5,6]]
print(verifica_diagonais(M))
Resposta:
True
Pois, diagonal principal: 1 + 3 + 6 = 10
diagonal secundária: 3 + 3 + 4 = 10'''

def cria_matriz():
    matriz = []
    i = 0
    j = 0
    while j <3:

        while i < 3:
            linha = []
            n = input("Insira um número")
            linha.append(n)
            i += 1

        matriz.append(linha)

    j += 1
    return matriz

a = cria_matriz()
print(a)

# def verifica_diagonais(matriz):
#     soma_diagonal_principal = matriz[0][0] + matriz[1][1] + matriz[2][2]
#     soma_diagonal_secundaria = matriz[0][2] + matriz[1][1] + matriz[2][0]
    
#     if soma_diagonal_principal >= soma_diagonal_secundaria:
#         return True
#     else:
#         return False

# # Uso da função
# matriz = cria_matriz()
# if matriz:
#     resultado = verifica_diagonais(matriz)
#     print("A soma da diagonal principal é maior ou igual à soma da diagonal secundária?", resultado)
