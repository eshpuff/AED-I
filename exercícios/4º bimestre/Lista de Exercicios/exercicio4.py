import random

baralho = []

naipes = ['Copas', 'Espadas', 'Ouros', 'Paus']
for naipe in naipes:
    for valor in range(1, 14):
        baralho.append(f'{valor} de {naipe}')

for i in range(len(baralho) - 1, 0, -1):
    j = random.randint(0, i)
    baralho[i], baralho[j] = baralho[j], baralho[i]

for carta in baralho:
    print(carta)

