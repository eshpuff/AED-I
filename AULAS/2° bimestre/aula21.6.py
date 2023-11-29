# in testa se uma string ta contida em outra
# nome = input("Insira um nome: ")

# if "garim" in nome:
#     print("Sim")
# else:
#     print("Não")

'''Dado um texto tem que verificar se essa frase tem todas as letras do alfabeto'''

texto = input("Insira uma frase: ")
alfabeto ="abcdefghijklmnopqrstuvwxyz"
cont = 0
soma = 0



while cont != 26:
    if alfabeto[cont] in texto:
        soma += 1
    cont+= 1

if soma == 26:
    print("O texto contém todas as letras do alfabeto")

else:
    print("Não contém todas letras do alfabeto.")
