# 20) Faça um programa em Python que simule um lançamento de um dado. Lance o dado
# 100 vezes e armazene os resultados em uma lista. Depois, mostre quantas vezes cada valor
# foi conseguido. Use uma lista para armazenar os resultados da contagem de cada valor (1-6)
# e uma função para gerar números aleatórios, simulando os lançamentos do dado.

import random

dices = []

def rollDice(qtd):
    for i in range(1, qtd+1):
        dices.append(random.randint(1,6))

rollDice(100)
    
d1=0
d2=0
d3=0
d4=0
d5=0
d6=0

for i in dices:
    if i == 1:
        d1+=1
    if i == 2:
        d2+=1    
    if i == 3:
        d3+=1    
    if i == 4:
        d4+=1    
    if i == 5:
        d5+=1    
    if i == 6:
        d6+=1        

print(f"O valor 1 apareceu {d1} vezes.")
print(f"O valor 2 apareceu {d2} vezes.")
print(f"O valor 3 apareceu {d3} vezes.")
print(f"O valor 4 apareceu {d4} vezes.")
print(f"O valor 5 apareceu {d5} vezes.")
print(f"O valor 6 apareceu {d6} vezes.")