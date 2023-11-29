''' Escreva um programa de adivinhação de número. O programa deve conter um número secreto entre 1 e 1.000.000. O usuário deve chutar um número e o programa 
deve dizer se o número chutado é maior ou menor que o número secreto. O usuário deve tentar até acertar o número secreto. O código abaixo mostrar como
sortear um número aleatório entre 0 e 10 em python:'''

#import random
#sorteado = random.randint(0,10)

import random
sorteado = random.randint(0,1000000)

chute = int(input("Advinhe o número: "))

while chute != sorteado:
    print("Errou.")
    if chute > sorteado:
        print("O número é menor que",chute)
    if chute < sorteado:
        print("O número é maior que",chute)

    chute = int(input("Advinhe o número: "))

print("Acertou.")