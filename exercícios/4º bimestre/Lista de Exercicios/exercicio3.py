def atualizarPontuacao(pontuacao, nome, pontos):
    pontuacao[nome] += pontos

pontuacao = {"Du": 0, "Dudu": 0, "Edu": 0}

print("Começou o jogo!!!!")

rodada = input("Para continuar insira 'sim' caso queria parar insira 'não', se quiser ver pontuação insira 'pontuação'.")

while rodada != "não":
    if rodada == "pontuação":
        print(pontuacao)

    nome = input("Insira nome do jogador: ")
    pontos = int(input("Insira pontuação dp jogador: "))
    
    atualizarPontuacao(pontuacao, nome, pontos)
    
    rodada = input("Adcionar outra rodada? ")

print("FIMMMM, pontuação final: ", pontuacao)