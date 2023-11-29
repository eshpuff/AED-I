''' Escreva um programa que leia diversos números até que o usuário digite zero. Em
seguida escreva a média dos números digitados.'''

n = int(input("Insira um número: "))
s = 0
q = 0


while n != 0:
    q += 1
    s += n
    n = int(input("Insira um número: "))

m = s / q

print("A média é: ",m)
