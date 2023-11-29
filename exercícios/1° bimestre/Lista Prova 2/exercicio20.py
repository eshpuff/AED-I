'''Faça um programa em python que leia um valor inteiro X. Em seguida apresente os 6
valores ímpares consecutivos a partir de X, inclusive o X se for o caso. Por exemplo,
para o número 8, a saída será “9,11,13,15,17,19”.'''

x = int(input("Insira um número: "))
i = 0

if x%2 == 0:
    x = x + 1
    while i < 6:
        print(x)
        i = i + 1
        x = x + 2

if x%2 != 0:
    while i < 6:    
        print(x)
        i = i + 1
        x = x + 2

##

x = int(input("Insira o valor de x: "))
i = 1

if x % 2 == 0:
    x +=1
    
while i <= 6:
    if x % 2 != 0:
        print (x)
        x += 2
        i += 1
