'''Faça um programa em python que pergunte ao usuário o seguinte: a) A viagem custará menos de R$ 30? b) Terá Wifi? c) Terá piscina?
d) Terá churrasqueira? O programa deverá mostrar se a viagem ocorrerá de acordo com as seguintes regras: - Deverá custar menos de R$ 30
- Tem que ter wifi e piscina - Se não tiver wifi ou piscina, tem que ter churrasqueira'''

price= float(input("Qual valor? "))

if price >30:
    print("Não tem férias, valor acima do orcamento.")
else:
    churras= input("Tem churrasqueira?")
    if churras == "sim":
        print("Baita! Bom rolê.")
    else:
        pool= input("Tem psicina?")
        wifi= input("Tem wi-fi?")
        if (pool == "sim" and wifi == "não") or (pool == "não" and wifi == "sim") or (pool == "não" and wifi == "não"):
            print("Não tem férias, rolê não atende as espectativas")
        else:
            print("Baita! Bom rolê.")
