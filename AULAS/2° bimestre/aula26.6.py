'''# listas
# tipos estruturados

# armazena qualquer tipo de dado

# mutável

# tipo variado

#compras = ['arroz', 'feijão', 'creatina', 'whey'] # cria uma lista na variável compras
#compras[2] = 'bomba' # transforma 'creatina' em 'bomba'
#compras.append('óleo') # adiciona 'óleo' na lista de compras.

#print(compras)

#megasena = []
#x = 10
#while x != '0':
#    x = input("num")
#    megasena.append(x)

#print(megasena)

# 1) CRIE UM PROGRAMA QUE FAÇA UMA LISTA DE COMPRAS.

compras = []
x = 10
while x != '':
    x = input('Digite um item para a lista de compras.\nPara finalizar a lista apenas confirme sem digitar nada.')
    if x != '':
        compras.append(x)
        print("Suas compras até então são:\n" + str(compras))

print('Sua lista de compras:\n' + str(compras))

# 2) VERIFIQUE SE UMA COMPRA ESTÁ NA LISTA.

y = 10
while y != '':
    y = input('Digite o que deseja pesquisar na lista.\nPara finalizar a busca apenas confirme sem digitar nada.')
    if y in compras:
        print(y, 'está na lista.')
    else:
        print(y, 'não está na lista.')

# Da para fazer com FOR IN também.

# 2)...

#busca = input('Digite o que deseja pesquisar na lista.')
#achei = False

#for item in compras:
#   if item == busca:
#       achei == True

#if achei:
#   print("O item está na lista.")
#else:
#   print("O item não está na lista.")'''

''' exercicio:
1) Crie uma lista com nome dos colegas.
2) Sorteie 5 colegas para um prêmio.'''

import random
colegas = ['Murilo', 'Victor', 'Christian', 'Marina', 'Sabrina', 'Bruno', 'Éshiley', 'Eric', 'Andrew', 'Lucas', 'Augusto', 'Aythana', 'Babi', 'Bernardo', 'Bruno', 'CB', 'Duds', 'Fabi', 'Felipe', 'Henrique', 'Paula', 'Tiago', 'Vicenzo', 'Arthur', 'Duda', 'Emy', 'Gabriel', 'JK', 'Medina', 'Vitória', 'Milena', 'Tiago']
premiados = []
premios = ['Netbook', 'Ônix', 'Férias no Caríbe', 'Café', 'R$250,00']

for index in range(5):
    y = random.randint(0,31)

    while y in premiados:
        y = random.randint(0,31)

    premiados.append(y)

index = 0
print("Os premiados são:")

for index in range(5):
    print(str(colegas[premiados[index]]), 'que foi premiado', premios[index])