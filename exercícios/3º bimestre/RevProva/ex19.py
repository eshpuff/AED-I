# 19) A Furg está tendo problemas de espaço em disco no seu servidor de arquivos. Para
# tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço
# ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um
# programa obtido na Internet, ele conseguiu gerar o seguinte arquivo, chamado
# "usuarios.txt":
# alexandre 456123789
# anderson 1245698456
# antonio 123456456
# carlos 91257581
# cesar 987458
# rosemary 789456125
# Neste arquivo, o nome do usuário possui exatamente 15 caracteres. A partir deste arquivo,
# você deve criar um programa em Python que gere um relatório, chamado "relatório.txt", no
# seguinte formato:
# Furg Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr. Usuário Espaço utilizado % do uso
# 1 alexandre 434,99 MB 16,85%
# 2 anderson 1187,99 MB 46,02%
# 3 antonio 117,73 MB 4,56%
# 4 carlos 87,03 MB 3,37%
# 5 cesar 0,94 MB 0,04%
# 6 rosemary 752,88 MB 29,16%
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# A conversão do espaço ocupado em disco, de bytes para megabytes, deverá ser feita através
# de uma função separada, que será chamada pelo programa principal. O cálculo do
# percentual de uso também deverá ser feito através de uma função, que será chamada pelo
# programa principal.

arq = open("ex19.txt", "r")
lines = arq.readlines()

def convertMega(byte):
    return int(byte)/1000000

def formatName(name):
    if len(name) > 15:
        while len(name) > 15:
            name = name.replace(name[len(name)-1], "", 1)
        return name
    elif len(name) == 0:
        return print("O nome deve possuir no mínimo 1 caractere.")
    elif len(name) == 15:
        return name
    else:
        while len(name) < 15:
            name+=" "
        return name

def percentage(total, mega):
    return (mega*100)/total

    
text_1 = '''Furg Uso do espaco em disco pelos usuarios
------------------------------------------------------------------------
Nr. Usuario Espaco utilizado % do uso
'''

text_2 = ""
total = 0
count = 0

for i in lines:
    megaBites = convertMega(i.split(" ")[1])
    total += megaBites

for i in lines:
    name = formatName(i.split(" ")[0])
    megaBites = convertMega(i.split(" ")[1])
    megaPerc = percentage(total, megaBites)
    count += 1

    text_2 += str(count)+" "
    text_2 += str(name)+" "
    text_2 += f'{megaBites:.2f} MB'+" "
    text_2 += f'{megaPerc:.2f}%'
    text_2 += "\n"
    
text_2 += f"Espaco total ocupado: {total:.2f} MB\n"
text_2 += f"Espaco medio ocupado: {total/6:.2f} MB\n"

report = text_1 + text_2

relatorio = open("relatorio.txt", "w")
relatorio.write(report)


    
# result = percentage(2581.57, float(convertMega(456123789)))
# print(f"{result:,.2f}"+"%")
    