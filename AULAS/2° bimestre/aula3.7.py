'''
str = "nome1;nome2;nome3"
resposta = str.split(" ")

print(resposta)
'''

# SPLIT
nome = input("Type your name! ")

list = nome.split(" ")
print(list)

ingles = list[-1] + ","

c = 0
while c < len(list)-1:
    if c+1 == len(list)-1:
        if list[c].lower() != "do" and list[c].lower() != "da" and list[c].lower() != "dos" and list[c].lower() != "das" and list[c].lower() != "de":
            ingles = ingles + " " + list[c]
    else: 
        ingles = ingles + " " + list[c]

    c = c + 1

print(ingles)

# JOIN

list = ['Ezio', 'Auditore', 'Da Firenze']
nome = " ".join(list)

print(nome)


# OUTRAS FUNÇÕES
# lower() - deixa tudo minúsculo
# upper() - deixa tudo maiúsculo
# capitalize() - deixa as primeiras letras maiúsculas

nome = input("Manda bala ")
nome = nome.lower().split(" ")

c = 0
while c < len(nome):
    if nome[c] != "do" and nome[c] != "da" and nome[c] != "dos" and nome[c] != "das" and nome[c] != "de":
        nome[c] = nome[c].capitalize()
    c = c + 1


nome = " ".join(nome)
print(nome)

# find - procura na string

str = "Victor Amaral"
resposta = str.find("a")
print(resposta) # 9