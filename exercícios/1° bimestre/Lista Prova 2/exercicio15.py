'''Escreva um programa que mostre a sequência de Fibonacci até o enésimo termo (n deve ser informado pelo usuário). A sequência de Fibonacci é aquela em que cada
termo é a soma dos dois termos anteriores. Por exemplo, para n=8 escreva 0, 1, 1, 2, 3, 5, 8 e 13.'''

entrada = int(input("Insira o número: "))
n1 = 0
n2 = 1
cont = 0

while cont < entrada:
    print(n1, end=', ')
    proximo = n1 + n2
    n1 = n2
    n2 = proximo
    cont = cont + 1