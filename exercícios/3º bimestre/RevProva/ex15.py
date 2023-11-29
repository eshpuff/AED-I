# 15) Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa cidade,
# em um determinado dia. Em um arquivo texto é fornecido, para cada casa visitada, o
# número do canal (4, 5, 7, 12) e o número de pessoas que o estavam assistindo naquela casa,
# separados por ponto e vírgula. Se a televisão estivesse desligada, nada era anotado, ou seja,
# esta casa não entrava na pesquisa. Faça uma função, em Python, que receba dois
# parâmetros, o nome do arquivo com os dados e o número do canal, e retorne a
# porcentagem de audiência deste canal.

def audience(archive, channel):
    arq = open(archive, "r")
    lines = arq.readlines()
    
    channelNum = channel
    channelCount = 0
    totalSum = 0
    
    for i in lines:
        totalSum+=int(i.split(";")[1])
        if i.split(";")[0] == channelNum:
            channelCount+=int(i.split(";")[1])
    return (channelCount*100)/totalSum

percent = audience("ex15.txt", "12")

print(f"O percentual de audiencia é de {percent:,.2f}%")

