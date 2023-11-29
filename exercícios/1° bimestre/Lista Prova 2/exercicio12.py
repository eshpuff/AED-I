''') Escreva um programa que mostre a seguinte sequência de números para um valor N informado pelo usuário:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
…
N N N N N N N …'''

n = int(input("Insira um número: "))
i = 0

while i < n:
    i = i + 1
    r = str(i)
    print(i*r)

