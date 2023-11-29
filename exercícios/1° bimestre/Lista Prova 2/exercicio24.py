'''Construa um programa em Python que escreva uma contagem de 10 (dez) minutos, ou seja, mostre 0:00, e então 0:01, 0:02, ..., 0:58, 0:59, 1:00, 1:01, ..., 
até 10:00.'''

min = 0
seg = 0

while min != 10:
    if seg == 60:
        min += 1
        seg = 0
    print(f"{format(min, '02d')}:{format(seg, '02d')}")
    seg += 1