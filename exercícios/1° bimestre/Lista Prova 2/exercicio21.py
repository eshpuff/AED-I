'''Escreva um programa que leia dois valores x e y. Em seguida escreva quais são os números primos contidos neste intervalo. Por exemplo, 
para x=3 e y=14 escreva: 3,5,7,11,13. Verifique se o usuário digitou x e y de modo que x<y.'''

x = int(input("Insira o valor x:"))
y = int(input("Insira o valor y:"))

while x > y:
    x = int(input("Insira um valor válido para x:"))


resto = ''
i = 2
p = 0

while x < y:
    while i < x:
        if x % i != 0:
            p = "primo"
        else:
            p = "Não primo"
            i = x
        i += 1
    if p == "primo":
        resto += str(x)+" "
    i = 2
    x += 1

print(resto)