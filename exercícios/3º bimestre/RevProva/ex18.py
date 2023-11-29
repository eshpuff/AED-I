# 18) Faça um programa em Python que receba a temperatura média de cada mês de um
# determinado ano, e armazene-as em uma lista. Em seguida, calcule a média anual das
# temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da
# média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
# Fevereiro, . . . ).

month = []

jan = month.append(input("Insira a temperatura de janeiro: "))
feb = month.append(input("Insira a temperatura de fevereiro: "))
mar = month.append(input("Insira a temperatura de março: "))
apr = month.append(input("Insira a temperatura de abril: "))
may = month.append(input("Insira a temperatura de maio: "))
june = month.append(input("Insira a temperatura de junho: "))
july = month.append(input("Insira a temperatura de julho: "))
aug = month.append(input("Insira a temperatura de agosto: "))
sept = month.append(input("Insira a temperatura de setembro: "))
oct = month.append(input("Insira a temperatura de outubro: "))
nov = month.append(input("Insira a temperatura de novembro: "))
dec = month.append(input("Insira a temperatura de dezembro: "))

calc = 0

for i in month:
    calc += float(i)
    
average = calc/12
cont = 0

print("Meses com temperaturas acima da média: ")

for i in month:
    if float(i) > average:
        if cont == 0:
            print(f"1-Janeiro: {float(i):,.2f}°C")
        elif cont == 1:
            print(f"2-Fevererio: {float(i):,.2f}°C")
        elif cont == 2:
            print(f"3-Março: {float(i):,.2f}°C")
        elif cont == 3:
            print(f"4-Abril: {float(i):,.2f}°C")
        elif cont == 4:
            print(f"5-Maio: {float(i):,.2f}°C")
        elif cont == 5:
            print(f"6-Junho: {float(i):,.2f}°C")
        elif cont == 6:
            print(f"7-Julho: {float(i):,.2f}°C")
        elif cont == 7:
            print(f"8-Agosto: {float(i):,.2f}°C")
        elif cont == 8:
            print(f"9-Setembro: {float(i):,.2f}°C")
        elif cont == 9:
            print(f"10-Outubro: {float(i):,.2f}°C")
        elif cont == 10:
            print(f"11-Novembro: {float(i):,.2f}°C")
        elif cont == 11:
            print(f"12-Dezembro: {float(i):,.2f}°C")
    cont += 1
    
print(f"A média das temperaturas foi de: {average:,.2f}°C")