'''Faça uma função em Python que receba, por parâmetro, um número inteiro x > 0, e
retorne o número de divisores positivos que x tem. Por exemplo: o número 12 tem 6
divisores (1, 2, 3, 4, 6 e 12).'''

x = int(input("Insert a number: "))

def countingDivider(x):
    cont = 0
    divList = []

    if x <= 0:
        print("Insert a divisible number.")

    else:
        for divider in range(1, x + 1):
            if x % divider == 0:
                divList.append(divider)
                cont += 1
        print("Maximum divisors from your number are:", divList)
countingDivider(x)

