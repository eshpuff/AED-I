'''Faça um programa em Python para ler “n” números inteiros, armazenando-os em uma lista (o usuário informará um valor inteiro positivo para “n”). Após, crie duas outras listas a partir desta primeira digitada, sendo que uma conterá os números positivos (>= 0), e a outra  conterá os números negativos. Mostre na tela como ficaram as três listas.'''
'''Baseado no programa anterior, remova todas as ocorrências do valor zero na lista dos números positivos. Mostre na tela as três listas, informando a quantidade de zeros que havia, o total de números remanescentes na lista de positivos e na de negativos. '''

n = input("Insira um número: ")
i = 0
zeros = 0
lista_og = []
lista_po = []
lista_ne = []
lista_og.append(n)


while n != "1000":
    n = input("Insira um número. ('1000' para sair): ")
    lista_og.append(n)
    i += 1

for num in lista_og:
    n = int(num)
    if n >= 0:
        lista_po.append(n)
    else:
        lista_ne.append(n)

for num in lista_po:
    if num == 0:
        zeros += 1
        lista_po.remove(num)

print("Numeros digitados:",lista_og)
print("Quantidade de 0 digitados:",zeros)
print("Numeros positivos:",lista_po)
print("Numeros negativos:",lista_ne)


