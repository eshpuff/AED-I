'''Construa um programa em Python para determinar e mostrar o número de dígitos de um número inteiro positivo informado.'''

n = int(input("Informe um número: "))
i = 0

if n == 0:
    i = 1
else:
    while n != 0:
        i += 1
        n //= 10

print("O número de digitos é",i)
