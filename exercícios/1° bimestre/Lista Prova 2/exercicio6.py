'''Faça um programa em python que leia o nome de 4 times de futebol que estão em uma semifinal. Após, leia os gols das duas partidas: 
time 1 x time 2 e time 3 x time 4. Os times vencedores devem ir para a final. Caso haja empate, deve-se perguntar ao usuário qual time 
se classificou. Por fim, deve-se ler os gols da final e mostrar qual time foi campeão (se empatar, perguntar quem foi campeão).'''

time1 = input("Insira o nome do primeiro time: ")
time2 = input("Insira o nome do segundo time: ")
time3 = input("Insira o nome do terceiro time: ")
time4 = input("Insira o nome do quarto time: ")

final1 = ""
final2 = ""

print(time1," x ",time2)
gols1 = int(input("Insira o número de gols do time "+time1+": "))
gols2 = int(input("Insira o número de gols do time "+time2+": "))


if gols1 > gols2:
    print("Time "+time1+" está na final." )
    final1 = time1
if gols2 > gols1:
    print("Time "+time2+" está na final.")
    final1 = time2
if gols1 == gols2:
    final1 = input("Insira o time vencedor: ")
    print("Time "+final1+" está na final.")

print(time3," x ",time4)
gols3 = int(input("Insira o número de gols do time "+time3+": "))
gols4 = int(input("Insira o número de gols do time "+time4+": "))

if gols3 > gols4:
    print("Time "+time3+" está na final." )
    final2 = time3
if gols4 > gols3:
    print("Time "+time4+" está na final.")
    final2 = time4
if gols4 == gols3:
    final2 = input("Insira o time vencedor: ")
    print("Time "+final2+" está na final.")

print(final1," x ",final2)
golsf1 = int(input("Insira o número de gols do time "+final1+": " ))
golsf2 = int(input("Insira o número de gols do time "+final2+": "))

if golsf1 > golsf2:
    print("Time "+final1+" ganhou o campeonato.")
if golsf2 > golsf1:
    print("Time "+final2+" ganhou o campeonato.")
if golsf1 == golsf2:
    ganhador= input("Insira o time vencedor: ")
    print("Time "+ganhador+" ganhou o campeonato.")

