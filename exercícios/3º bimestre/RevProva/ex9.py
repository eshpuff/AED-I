##chatgpt oppa.. *- ((meu cerebro ja tava pedindo socorro.))

'''9) Faça um programa em Python para jogar o “jogo da velha”. O algoritmo deve permitir que
dois jogadores joguem uma partida, usando o computador para ver o tabuleiro. Cada
jogador vai alternadamente informando a posição onde deseja colocar a sua peça (O ou
X). O programa deverá impedir jogadas inválidas, e determinar automaticamente quando o
jogo terminou, e quem foi o vencedor (jogador1 ou jogador2). A cada nova jogada, o
programa deve atualizar a situação do tabuleiro na tela.'''

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    print("joga")

    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1 ou 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2): "))

        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2 or tabuleiro[linha][coluna] != " ":
            print("Jogada inválida. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if jogadas == 9:
            imprimir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

jogar_jogo_da_velha()