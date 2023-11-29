'''Crie um programa que recebe uma string como entrada e retorna uma nova string em que cada caractere foi substituído pelo seu código ASCII. Exemplo: # Informe o texto: Hello # Saída esperada: "72 101 108 108 111" '''

string = input("Informe o texto: ")
lista = []
tamanho = 0
i = 0

while tamanho < len(string):
    ascii = ord(string[i])
    lista.append(ascii)
    tamanho += 1 
    i += 1

print(lista)