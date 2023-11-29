def verifica_fim_jogo(tabuleiro):
    # Conta o número de pinos no tabuleiro
    num_pinos = 0
    for linha in tabuleiro:
        num_pinos += sum(linha)
    
    # Se houver exatamente um pino no tabuleiro, o jogo chegou ao fim
    return num_pinos == 1

# Exemplo de uso
tabuleiro_exemplo = [
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0]
]

resultado = verifica_fim_jogo(tabuleiro_exemplo)
print("O jogo chegou ao fim?", resultado)
