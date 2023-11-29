# Crie um programa em Python que leia o rendimento mensal do usuário, qual o modelo de
# de imposto (sem correção/com correção das perdas no governo Bolsonaro) e retorne
#  o quanto ele deve pagar de imposto

renda= float(input("Insira o seu rendimento mensal: "))
modelo= int(input("Se o modelo for sem correção, insira 1. \nSe o modelo for com correção no gov Bolsonaro, insira 2." ))

# modelo sem correção
imposto = 0
deduzido = 0

if modelo == 1:
    if renda <= 1903.98:
        print("Isento.")
    if 1903.98 < renda <= 2826.65:
        imposto = (renda * 7.5) / 100
        deduzido = imposto - 142.80
        print("O imposto de renda é:", round(deduzido, 2))
    if 2826.65 < renda <= 3751.05:
        imposto = (renda * 15) / 100
        deduzido = imposto - 354.80
        print("O imposto de renda é:", round(deduzido, 2))
    if 3751.05 < renda <= 4664.68:
        imposto = (renda * 22.5) / 100
        deduzido = imposto - 636.13
        print("O imposto de renda é:", round(deduzido, 2))
    if renda > 4664.68:
        imposto = (renda * 27.5) / 100
        deduzido = imposto - 869.36
        print("O imposto de renda é:", round(deduzido, 2))

# modelo Bolsonaro
if modelo == 2:
    if renda <= 2500.44:
        print("Isento.")
    if 2500.44 < renda <= 3712.17:
        imposto = (renda * 7.5) / 100
        deduzido = imposto - 187.54
        print("O imposto de renda é:", round(deduzido, 2))
    if 3712.17 < renda <= 4926.14:
        imposto = (renda * 15) / 100
        deduzido = imposto - 465.95
        print("O imposto de renda é:", round(deduzido, 2))
    if 4926.14 < renda <= 6125.99:
        imposto = (renda * 22.5) / 100
        deduzido = imposto - 835.41
        print("O imposto de renda é:", round(deduzido, 2))
    if renda > 6125.99:
        imposto = (renda * 27.5) / 100
        deduzido = imposto - 1141.71
        print("O imposto de renda é:", round(deduzido, 2))