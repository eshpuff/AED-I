'''Leia uma matriz e mostre na tela no formato para humano.'''

menu = input("Insira a primeira linha da matriz (para sair digite sair): ").lower()
lista = []
lista2 = menu.split()
lista.append(lista2)
tamanho = len(lista2)
i = 0

while menu != "sair": # criando matriz
    menu = input("Insira a próxima linha da matriz (para sair digite sair): ").lower()
    lista2 = []
    lista2 = menu.split()
    lista.append(lista2)
    lista2 = []

lista = lista[:-1] # tirando o sair

for linha in lista: # printo
    if len(linha) != tamanho:
        print("Erro! Matriz invalida.")
    else:
        print("|"," ".join(lista[i]),"|")
    i += 1

a = int(lista[0][0]) * int(lista[1][1]) * int(lista[2][2])
b = int(lista[0][1]) * int(lista[1][2]) * int(lista[2][0])
c = int(lista[0][2]) * int(lista[1][0]) * int(lista[2][1])
d = int(lista[0][2]) * int(lista[1][1]) * int(lista[2][0])
e = int(lista[0][0]) * int(lista[1][2]) * int(lista[2][1])
f = int(lista[0][1]) * int(lista[1][0]) * int(lista[2][2])

determinante = a + b + c - d - e - f
print(determinante)

# multiplica matriz e enviar pdf