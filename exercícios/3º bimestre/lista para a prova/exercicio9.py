print("Jogo da Velha!")
jogador1 = "X"
jogador2 = "O"

linha1 = [" ", " ", " "]
linha2 = [" ", " ", " "]
linha3 = [" ", " ", " "]

result = False

def mostrar_tabuleiro():
    print("  1 | 2 | 3 ")
    print("---------")
    print(f"A {linha1[0]} | {linha1[1]} | {linha1[2]}   ")
    print("---------")
    print(f"B {linha2[0]} | {linha2[1]} | {linha2[2]}   ")
    print("---------")
    print(f"C {linha3[0]} | {linha3[1]} | {linha3[2]}   ")

def verificar_vitoria():
    for linha in [linha1, linha2, linha3]:
        if linha[0] == linha[1] == linha[2] != " ":
            return True

    for coluna in range(3):
        if linha1[coluna] == linha2[coluna] == linha3[coluna] != " ":
            return True

    if linha1[0] == linha2[1] == linha3[2] != " " or linha1[2] == linha2[1] == linha3[0] != " ":
        return True

    return False

while not result:
    mostrar_tabuleiro()
    jogador1_posicao = input(f"Jogador 1 ({jogador1}), informe a posição (por exemplo, 'A1'): ")
    if jogador1_posicao == "A1" and linha1[0] == " ":
        linha1[0] = jogador1
    elif jogador1_posicao == "A2" and linha1[1] == " ":
        linha1[1] = jogador1
    elif jogador1_posicao == "A3" and linha1[2] == " ":
        linha1[2] = jogador1
    elif jogador1_posicao == "B1" and linha2[0] == " ":
        linha2[0] = jogador1
    elif jogador1_posicao == "B2" and linha2[1] == " ":
        linha2[1] = jogador1
    elif jogador1_posicao == "B3" and linha2[2] == " ":
        linha2[2] = jogador1
    elif jogador1_posicao == "C1" and linha3[0] == " ":
        linha3[0] = jogador1
    elif jogador1_posicao == "C2" and linha3[1] == " ":
        linha3[1] = jogador1
    elif jogador1_posicao == "C3" and linha3[2] == " ":
        linha3[2] = jogador1
    else:
        print("Posição inválida. Tente novamente.")
        continue

    result = verificar_vitoria()
    if result:
        mostrar_tabuleiro()
        print("Jogador 1 venceu!")
        break

    mostrar_tabuleiro()
    jogador2_posicao = input(f"Jogador 2 ({jogador2}), informe a posição (por exemplo, 'A1'): ")
    if jogador2_posicao == "A1" and linha1[0] == " ":
        linha1[0] = jogador2
    elif jogador2_posicao == "A2" and linha1[1] == " ":
        linha1[1] = jogador2
    elif jogador2_posicao == "A3" and linha1[2] == " ":
        linha1[2] = jogador2
    elif jogador2_posicao == "B1" and linha2[0] == " ":
        linha2[0] = jogador2
    elif jogador2_posicao == "B2" and linha2[1] == " ":
        linha2[1] = jogador2
    elif jogador2_posicao == "B3" and linha2[2] == " ":
        linha2[2] = jogador2
    elif jogador2_posicao == "C1" and linha3[0] == " ":
        linha3[0] = jogador2
    elif jogador2_posicao == "C2" and linha3[1] == " ":
        linha3[1] = jogador2
    elif jogador2_posicao == "C3" and linha3[2] == " ":
        linha3[2] = jogador2
    else:
        print("Posição inválida. Tente novamente.")
        continue

    result = verificar_vitoria()
    if result:
        mostrar_tabuleiro()
        print("Jogador 2 venceu!")
        break

print("Fim do jogo!")
