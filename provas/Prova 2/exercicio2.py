'''Crie um programa em Python que imprima uma sequência de números em forma de pirâmide. O programa deve solicitar ao usuário um número inteiro
positivo e, em seguida, imprimir os números de 1 até o número informado, em linhas crescentes e decrescentes, formando uma pirâmide.
Exemplo:
Digite um número inteiro positivo: 4
1
12
123
1234
4321
321
21
1'''

n = int(input("Digite um número inteiro positivo: "))
andar = n * 2
i = 0
m = 0


while i < n:
    i += 1
    m = str(i)
    print(i * m)

i = n + 1

while i > 1:
    i -= 1
    m = str(i)
    print(i * m)



        