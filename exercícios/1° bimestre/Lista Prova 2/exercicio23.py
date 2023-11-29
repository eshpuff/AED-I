'''Considere uma sequência de números que atende a todos critérios abaixo: 
a - Possui sempre 2 dígitos , nem mais , nem menos . 
b - A representação do número possui pelo menos um dígito 1 ou um dígito 2. 
c - O número é múltiplo de 3. Faça um programa que implemente e mostre essa sequência. 
obs: tem que usar repetição
para mostrar a sequência. Não pode mostrar os números “na mão”'''

n = int(input("Insira um número: "))
i= 0
    
while i <= n:
    if i > 10 and i < 100:
        if i // 10 == 1 or i // 10 == 2 or i % 10 == 1 or i % 10 == 2:
            if i % 3 == 0:
                print (i)
    i += 1