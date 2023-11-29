'''Escreva um programa que receba um número inteiro positivo do usuário e verifique se ele é primo.'''

n = int(input("Insira um número: "))
i = 1
primo = 0

while i <= n:
    resto = n%i
    if resto == 0:
        primo += 1
    i = i + 1


if primo == 2:
    print("O número é primo.")

else:
    print("Não é primo.")
