'''Imagine que você está conduzindo um experimento científico em um laboratório e deseja analisar os dados coletados. Os dados são representados em forma de listas em um arquivo texto, e você precisa criar um programa em Python para realizar algumas operações de análise de dados. O arquivo possui o seguinte form
ato:
● 1a linha: uma lista de temperaturas medidas em graus Celsius, separadas por vírgula.
● 2a linha: uma lista de pressões medidas em Pascal, separadas por vírgula.
● 3a linha: uma lista de nomes dos experimentos correspondentes, separados por vírgula.
O programa deve ser capaz de ler esse arquivo e fazer o seguinte:
● Calcular a temperatura média e a pressão média a partir das listas. V
● Identificar qual experimento teve a maior temperatura máxima. 
● Identificar qual experimento teve a menor pressão mínima.
● Exibir todos os experimentos em que a temperatura seja superior a 25 graus Celsius.'''

def pressaoMedia(pressao):
    pressaomedia1 = 0
    for num in pressao:
        pressaomedia1 += num
    pressaomedia = pressaomedia1 / len(pressao)
    return pressaomedia
def temperaturaMedia(temperatura):
    temperaturamedia1 = 0
    for num in temperatura:
        temperaturamedia1 += num
    temperaturamedia = temperaturamedia1 / len(temperatura)
    return temperaturamedia
def maiorTemperatura(temperatura, nomes2):
    temperaturaMaior = 0
    for num in temperatura:
        if num > temperaturaMaior:
            temperaturaMaior = num
    i = 0
    while i < len(temperatura):
        if temperaturaMaior == temperatura[i]:
            nome = nomes2[i]
        i += 1    
    return nome

def menorPressao(pressao, nomes2):
    pressaoMenor = 0
    for num in pressao:
        if num > pressaoMenor:
            pressaoMenor = num
    i = 0
    while i < len(pressao):
        if pressaoMenor == pressao[i]:
            nomepressao = nomes2[i]
        i += 1    
    return nomepressao

# def maior25(temperatura, nomes2):
#     maior25 = []
#     i = 0
#     for coisa in temperatura:
#         i += 1
#         if int(temperatura[coisa]) > 25:
#             maior25.append(nomes2[i])

arquivo = open("ex1.csv","r")
a= 0

temperaturas = []
temperaturas.append(arquivo.readline())

temperatura = []
pressao = []
pressoes = []
pressoes.append(arquivo.readline())

nomes = []
nomes.append(arquivo.readline())

for i in temperaturas:
    temperaturas2 = i[:-1].split(",")
for i in pressoes:
    pressoes2 = i[:-1].split(",")
for i in nomes:
    nomes2 = i[:-1].split(",")

for i in temperaturas2:
    temperatura.append(int(i))

for i in pressoes2:
    pressao.append(int(i))


pressoesmedias = pressaoMedia(pressao)
print("A pressão média é:", pressoesmedias)
temperaturasmedias = temperaturaMedia(temperatura)
print("A temperatura média é:",temperaturasmedias)
temperturaAlta = maiorTemperatura(temperatura, nomes2)
print("O experimento que teve a maior temperatura máxima: ", temperturaAlta)
pressaoBaixa = menorPressao(pressao, nomes2)
print("O experimento que teve a menor pressão mínima", pressaoBaixa)

lista = []
for i in temperatura:
    cont = 0
    if i > 25:
        lista.append(i)

print("As temperaturas maiores que 25o são:",lista)
# print(temperaturas2, nomes2, pressoes2)
# print(temperatura, pressao)