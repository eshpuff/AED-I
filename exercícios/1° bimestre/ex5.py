'''Os números primos possuem várias aplicações dentro da Computação como, por exemplo, na Criptografia. Faça um programa em Python que
gere uma sequência de números primos existentes entre 1 e um número inteiro N informado pelo usuário (0 < N < 300).'''

n = int(input("Insira um número: "))
num = 2
i = 0

while num <= n:
    is_prime = 1
    i = 2
    while i <= int(num**0.5) and is_prime:
        if num % i == 0:
            is_prime = 0
        i += 1

    if is_prime:
        print(num)

    num += 1