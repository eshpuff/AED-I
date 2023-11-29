'''Faça uma função em Python que receba, por parâmetro, um número inteiro x > 0, e retorne o número de divisores positivos que x tem. Por exemplo: o número 12 tem 6 divisores (1, 2, 3, 4, 6 e 12).'''

x = int(input("Insira um número inteiro e maior que zero: "))
lista= []
i = 1

while i <= x:
    if x % i == 0:
        lista.append(i)
    i += 1

print("O numero", x, "tem",len(lista),"divisores.")