'''Implemente um programa em python que recebe um texto como entrada e realiza seguinte análise:                                                                                                                              a) Conte e mostre o número total de caracteres no texto (incluindo espaços em branco).                                                                                                                                b) Conte e mostre o número total de palavras no texto.                                                                                                                                c) Conte e mostre o número total de frases no texto.                                                                                Obs: considere que uma palavra é uma sequência de caracteres separada por espaços em branco e uma frase é uma sequência de palavras terminada por um ponto, ponto de exclamação ou ponto de interrogação'''

string = input("Insira um texto: ")
i = 0
palavras = 1
frases = 0

while i < len(string):
    if string[i] == " ":
        palavras += 1

    if string[i] == ".":
        frases += 1
    if string[i] == "!":
        frases += 1
    if string[i] == "?":
        frases += 1
    i += 1

print("O texto contém",len(string),"caracteres,",palavras,"palavras e",frases,"frases.")