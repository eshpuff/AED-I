'''Considere um programa em Python que simula um jogo de cartas com um baralho completo. O baralho é inicializado com 52 cartas, divididas em 4 naipes (Paus, Ouros, Copas e Espadas) e 13 valores (de 2 a 10, Valete, Dama, Rei e Ás). O programa deve utilizar listas para armazenar o baralho e sortear duas cartas para cada um de 6 jogadores. Mostre na tela cada uma das cartas sorteadas para cada jogador. Você não deve permitir que uma carta seja sorteada mais de uma vez.'''

baralho = ["às paus","2 paus","3 paus","4 paus","5 paus","6 paus","7 paus","8 paus","9 paus","10 paus","valete paus","dama paus","rei paus","às ouros","2 ouros","3 ouros","4 ouros","5 ouros","6 ouros","7 ouros","8 ouros","9 ouros","10 ouros","valete ouros","dama ouros","rei ouros","às copas","2 copas","3 copas","4 copas","5 copas","6 copas","7 copas","8 copas","9 copas","10 copas","valete copas","dama copas","rei copas","às espadas","2 espadas","3 espadas","4 espadas","5 espadas","6 espadas","7 espadas","8 espadas","9 espadas","10 espadas","valete espadas","dama espadas","rei espadas"]

jogador1 = []
jogador2 = []
jogador3 = []
jogador4 = []
jogador5 = []
jogador6 = []

i = 0 

import random

while len(jogador1) < 2:
    carta = random.randint(0,51)
    while carta in baralho:
        carta = random.randint(0,51)
    jogador1.append(carta)


for i in range(2):
    print("jogador 1:",str(baralho[jogador1[i]]))
i = 0 
 


while len(jogador2) < 2:
    carta = random.randint(0,51)
    while carta in baralho:
        carta = random.randint(0,51)
    if carta not in jogador1:
        jogador2.append(carta)



for i in range(2):
    print("jogador 2:",str(baralho[jogador2[i]]))
i = 0 


while len(jogador3) < 2:
    carta = random.randint(0,51)
    while carta in baralho:
        carta = random.randint(0,51)
    if carta not in jogador2:
        jogador3.append(carta)


for i in range(2):
    print("jogador 3:",str(baralho[jogador3[i]]))
i = 0 

while len(jogador4) < 2:
    carta = random.randint(0,51)
    while carta in baralho:
        carta = random.randint(0,51)
    if carta not in jogador3:
        jogador4.append(carta)


for i in range(2):
    print("jogador 4:",str(baralho[jogador4[i]]))
i = 0 


while len(jogador5) < 2:
    carta = random.randint(0,51)
    while carta in baralho:
        carta = random.randint(0,51)
    if carta not in jogador4:
        jogador5.append(carta)


for i in range(2):
    print("jogador 5:",str(baralho[jogador5[i]]))
i = 0 


while len(jogador6) < 2:
    carta = random.randint(0,51)
    while carta in baralho:
        carta = random.randint(0,51)
    if carta not in jogador5:
        jogador6.append(carta)



for i in range(2):
    print("jogador 6:",str(baralho[jogador6[i]]))
