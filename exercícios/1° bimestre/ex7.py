'''Escreva um programa em python que leia o horário (horas e minutos) de partida de um voo, o tempo de viagem e a diferença em horas do 
fuso horário do destino. O programa deve informar qual será o horário local no destino previsto para a chegada do voo. Lembrando que o 
voo pode chegar no dia seguinte.
Ex:
Informe o horário de partida (horas): 14
Informe o horário de partida (minutos): 00
Informe o tempo de viagem (horas): 1
Informe o tempo de viagem (minutos): 30
Informe o fuso horário (horas): 3
O horário previsto para chegada no destino é: 18:30'''

dh = int(input("Indique o horário em horas: "))
dm = int(input("Indique o horário em minutos: "))
th = int(input("Indique o tempo da viagem em horas: "))
tm = int(input("Indique o minuto do tempo de viagem: "))

h = dh + th
m = dm + tm

if m > 59:
    h += 1
    m -= 60

if h > 24:
    hh = h - 24
    print("O horário de chegada é",hh,":",m)

else:
    print("O horário de chegada é",h,":",m)