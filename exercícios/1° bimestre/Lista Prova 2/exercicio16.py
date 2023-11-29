'''Escreva um programa que calcule o fatorial de um número fornecido pelo usuário. O fatorial de um número n é o produto de todos os números inteiros de 1 a n.'''

n = int(input("Insira um número: "))
i = n


while n != 1:
    i *= n - 1
    n -= 1

print(i)