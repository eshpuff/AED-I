'''Faça um programa em python que desenhe uma pirâmide conforme 2 dados informados pelo usuário. O primeiro dado indica o "tijolo" e o segundo a quantidade
de andares.
Ex: Informe o tijolo: A
Informe a quantidade de andares: 5
A
AAA
AAAAA
AAAAAAA
AAAAAAAAA'''

tijolo = str(input("Informe o tijolo: ")).upper()
andares = int(input("Informe a quantidade de andares: "))
i = 1
m = 1

while i <= andares:
    print((andares-i) * " ",tijolo * m)
    m += 2
    i += 1
