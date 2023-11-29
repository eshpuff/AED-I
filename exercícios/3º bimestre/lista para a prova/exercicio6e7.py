''' Faça um programa em Python que leia duas listas de números compostas por cinco elementos informados de maneira ordenada (números em ordem crescente). Crie uma terceira lista também ordenada, sendo a união das duas primeiras listas. Exiba as listas, e a soma dos seus elementos contidos. '''
'''Altere o programa anterior para desprezar os números iguais, caso estes existam. Portanto, a lista final não deve possuir números iguais armazenados.'''

lista1 = []
lista2 = []
i = 0
j = 0


n1 = int(input("Insira valor: "))
lista1.append(n1)

while len(lista1) < 5:
    n1 = int(input("Insira valor maior que o valor anterior: "))
    lista1.append(n1)

n2 = int(input("Insira um valor: "))
lista2.append(n2)

while len(lista2) < 5:
    n2 = int(input("Insira um valor maior que o valor anterior: "))
    lista2.append(n2)

lista3 = []


while len(lista3) < 10:
    if i < 5 and j < 5:
        if lista1[i] < lista2[j]:
            lista3.append(lista1[i])
            i += 1
        elif lista1[i] > lista2[j]:
            lista3.append(lista2[j])
            j += 1
        else:
            lista3.append(lista1[i])
            i += 1
            j += 1
    elif i < 5:
        lista3.append(lista1[i])
        i += 1
    elif j < 5:
        lista3.append(lista2[j])
        j += 1


print(lista3)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista Unida (sem números iguais):", lista3)
