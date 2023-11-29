'''Você deve criar um jogo de dados em Python onde o jogador lança dois dados de seis faces e tenta adivinhar se a soma dos números nos dados será maior ou igual a um determinado valor escolhido. Implemente uma função chamada lançar_dados, que simula o lançamento de dois dados de seis faces (sortear) e retorna a soma dos resultados. Implemente uma função chamada validar_aposta, que verifica se a aposta do jogador é um número inteiro positivo entre 2 e 12.
Exemplo:
Bem-vindo ao Jogo de Dados!
Digite o valor alvo (2-12): 7
Lançando os dados...
Os números nos dados somam 8.
Você ganhou a aposta! A soma dos dados é maior ou igual a 7.'''

import random

validacao = False
dados = 0
i = 0

def lançar_dados(dados):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    # print(dado1, dado2)
    soma = dado1 + dado2
    return soma

def validar_aposta(i, aposta):
    while aposta <= 1 or aposta >= 13:
        print("Valor inválido.")
        aposta = int(input("Digite o valor do alvo (2-12): "))
        i += 1
    else:
        print("Lançando dados...")
    return aposta
    validacao = True
        

print("Bem-vindo ao Jogo de Dados!")
aposta = int(input("Digite o valor do alvo (2-12): "))

validacao = validar_aposta(i, aposta)
dados = lançar_dados(dados)

print("Os números nos dados somam",dados)

if validacao:
    if aposta <= dados:
        print("Você ganhou a aposta! A soma dos dados é maior ou igual a", aposta)
    if aposta > dados:
        print("Você perdeu a aposta bué-bué.")