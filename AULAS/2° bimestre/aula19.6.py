#ler cpf da pessoa e formatar-lo

cpf = input("Insira seu cpf: ")
formatado  = ""
i = 0
c = 10
verificador = 0
cont = 11
verificador2 = 0

while i < len(cpf):
    if i == 3:
        formatado += "."
    if i == 6:
        formatado += "."
    if i == 9:
        formatado += "-"

    formatado += cpf[i]
    i += 1


if len(cpf) == 11:
    i = 0
    while c >= 2:
        verificador += int(cpf[i])* c
        c -= 1
        i += 1
    verificador1 = (verificador * 10)%11
    i = 0
    while cont >= 2:
        verificador2 += int(cpf[i])* cont
        cont -= 1
        i += 1
    verificador3 = (verificador2 * 10)%11

else: 
    print("Informe cpf válido.")

if verificador1 == int(cpf[9]) and verificador3 == int(cpf[10]):
    print(formatado)

else:
    print("Informe cpf válido.")



