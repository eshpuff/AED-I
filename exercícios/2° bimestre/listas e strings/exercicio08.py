'''O algoritmo bag-of-words é uma representação simplificada usada no processamento de linguagem natural. Nesse modelo, um texto é representado como a bolsa de suas palavras, desconsiderando a gramática e até mesmo a ordem das palavras, mas mantendo a multiplicidade, ou seja, a quantidade de vezes que cada palavra aparece. Faça um programa em python que implemente o “bag-of-words”, contando quantas vezes cada palavra aparece em um texto e após construa um gráfico com o resultado.'''

bag_of_words = input("Insira um texto: ").split()
bolsinha = []
frequencia = []
i = 0
cont = 0

while i < len(bag_of_words):
    if bag_of_words[i] in bolsinha:
        posicao = bolsinha.index(bag_of_words[i])
        frequencia[posicao] += 1
    else:
        bolsinha.append(bag_of_words[i])
        frequencia.append(1)
    i += 1

print("Palavra : Frequência")
while cont < len(bolsinha):
    print(bolsinha[cont]+":",frequencia[cont])
    cont += 1