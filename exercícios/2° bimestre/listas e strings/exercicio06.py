'''Faça um programa que gerencie uma lista de times de futebol. Você precisa criar um programa que armazene uma lista de times de futebol. O programa deve permitir ao usuário adicionar novos times à lista, remover times existentes e exibir a lista completa de times. Crie um menu em que o usuário fique escolhendo a opção desejada.'''

times = []
x = 1

menu = input("Menu:\n Insira 1 para adicionar novos times. \n Insira 2 para remover times já existentes. \n Insira 3 para exibir lista completa.\n Insira 0 para finalizar.\n Resposta: ")

# Adicionar novos times:
if menu == "1":
    while x != '':
        x = input("Insira o nome do time (Para finalizar pressione enter sem digitar nada.): ")
        if x != '':
            times.append(x)
            print("Até agora, os times são:",times)
    menu = input("Menu:\n Insira 1 para adicionar novos times. \n Insira 2 para remover times já existentes. \n Insira 3 para exibir lista completa.\n Insira 0 para finalizar.\n Resposta: ")

# Remover times:
x = 1
if menu == "2":
    print("Os times já adicionados são:",times)
    while x != '':
        x = input("Insira nome do time que você quer remover. (Para finalizarr pressione enter sem digitar nada.): ")
        if x != '':
            times.remove(x)
            print("Até agora, os times são:",times)

    menu = input("Menu:\n Insira 1 para adicionar novos times. \n Insira 2 para remover times já existentes. \n Insira 3 para exibir lista completa.\n Insira 0 para finalizar.\n Resposta ")

# Exibir lista completa:
if menu == "3":
    print("A lista final de times é:", times)
    menu = input("Menu:\n Insira 1 para adicionar novos times. \n Insira 2 para remover times já existentes. \n Insira 3 para exibir lista completa.\n Insira 0 para finalizar. ")

# Fim: 
if menu == "0":
    print("FIM.")