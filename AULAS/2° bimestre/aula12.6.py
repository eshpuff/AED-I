'''nome = "éshiley"

for i in nome:
    print(i)'''

# print(ord("7"))
# print(chr(97))

nome = input("Insira um nome: ")
novo = " "
i = 0
maiusculo = " "
cont= 0

while i < len(nome):
    if ord(nome[i]) <= 90 and ord(nome[i]) > 64:
        novo = novo + chr(ord(nome[i]) + 32)
    else:
        novo = novo + nome[i]
    i += 1

while cont < len(novo):
    if novo[cont - 1] == " ":
        if (novo[cont] == "d" and novo[cont+1] == "a" and novo[cont+2] == " ") or (novo[cont] == "d" and novo[cont+1] == "o" and novo[cont+2] == " ") or (novo[cont] == "d" and novo[cont+1] == "e" and novo[cont+2] == " ") or (novo[cont] == "d" and novo[cont+1] == "o" and novo[cont+2] == "s"  and novo[cont+3] == " ") or (novo[cont] == "d" and novo[cont+1] == "a" and novo[cont+2] == "s" and novo[cont+3] == " "):
            maiusculo = maiusculo + novo[cont]
        else:
            maiusculo = maiusculo + chr(ord(novo[cont]) - 32)
        cont += 1
    if novo[cont] == 0:
        maiusculo = maiusculo + chr(ord(novo[cont]) - 32)
    else:
        maiusculo = maiusculo + novo[cont]
    cont += 1
print(maiusculo)

