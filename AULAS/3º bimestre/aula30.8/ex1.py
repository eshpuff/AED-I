qtd = int(input("Insira a tabuada: "))
linha = []
cont = 1

while cont < qtd + 1:
    linha.append(cont)
    cont += 1

tabela = ""

i = 1
x = 0

for numero in linha:
    tabela += str(i)
    for num in range(2,11):
        tabela += ";" + str(num*i)
    tabela += "\n"
    i += 1
    x = 0

print(tabela)

arq = open("ex.csv","w")
arq.write(tabela)
