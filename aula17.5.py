# #Leia as 4 notas, Leia a frequencia em %, média >= 7 -> passa poe média, 3<média<7 -> exame, media <=3 -> rodou, frequencia<75%-> rodou
# n1= float(input("Insira sua nota no 1o bimestre: "))
# n2= float(input("Insira sua nota no 2o bimestre: "))
# n3= float(input("Insira sua nota no 3o bimestre: "))
# n4= float(input("Insira sua nota no 4o bimestre: "))
# f= float(input("Insira a porcentagem de frequência: "))
# media= (n1+n2+n3+n4)/4

# if f>=75:
#     if media>=7:
#         print("Passou por média 🤩  com: "+str(media))
#     if media> 3 and media<7:
#         print("Esta em exame. 😠  Média: "+str(media))
#     if media<=3:
#         print("Rodou.👺")
# else:
#     print("Rodou por falta.👺")

# #Ler altura e largura; é uma medida válida(lados maior que zero); é um quadrado;  
# l= float(input("Insira largura: ")) 
# h= float(input("Insira altura:"))

# if h > 0 and l > 0:
#     if h==l:
#         print("È um quadrado.")
#     else:
#         print("É retângulo.")
# else:
#     print("Valores precisam ser maior que zero.")

# #Faça um programa em python que leia o nome de 4 times de futebol que estão emuma semifinal. Após, leia os gols das duas partidas: time 1 x time 2 e time 3 x time 4.
# # Os times vencedores devem ir para a final. Caso haja empate, deve-se perguntar ao
# # usuário qual time se classificou. Por fim, deve-se ler os gols da final e mostrar qual
# # time foi campeão (se empatar, perguntar quem foi campeão)

# t1= input("Insira nome do time 1: ")
# t2= input("Insira nome do time 2: ")
# t3= input("Insira nome do time 3: ")
# t4= input("Insira nome do time 4: ")

# g1= int(input("Insira numero de gols do "+t1+" : "))
# g2= int(input("Insira numero de gols do "+t2+" : "))

# f1= ""
# f2= ""

# if g1 > g2:
#     print("Time "+t1+" está na final.")
#     f1 = t1
# if g2 > g1:
#     print("Time "+t2+" está na final.")
#     f1 = t2
# if g1 == g2:
#     f1= input("Insira time vencedor: ")
#     print("Time "+f1+" está na final.")

# g3= int(input("Insira numero de gols do "+t3+": "))
# g4= int(input("Insira numero de gols do "+t4+": "))

# if g3 > g4:
#     print("Time "+t3+" está na final.")
#     f2 = t3
# if g4 > g3:
#     print("Time "+t4+" está na final.")
#     f2 = t4
# if g3 == g4:
#     f2= input("Insira time vencedor: ")
#     print("Time "+f2+" está na final.")

# gf1= int(input("Insira número de gols do "+f1+": "))
# gf2= int(input("Insira número de gols do "+f2+": "))

# if gf1 > gf2:
#     print("Time "+f1+" ganhou.")
# if gf2 > gf1:
#     print("Time "+f2+" ganhou.")
# if gf1 == gf2:
#     gf3= input("Insira time vencedor: ")
#     print("Time "+gf3+" ganhou.")
    
# # Crie um programa em Python que leia o rendimento mensal do usuário, qual o modelo de
# # de imposto (sem correção/com correção das perdas no governo Bolsonaro) e retorne
# #  o quanto ele deve pagar de imposto

# renda= float(input("Insira o seu rendimento mensal: "))
# modelo= int(input("Se o modelo for sem correção, insira 1. \nSe o modelo for com correção no gov Bolsonaro, insira 2. \nSe o modelo for com correção integral, insira 3. \n"))

# if modelo == 1:
#     if renda <= 1900:
#         print("Isento.")
#     else:
#         if renda < 2800:
#          print("Deve pagar R$142,80.")
#         else:
#             if renda < 4600:
#                 print("Deve pagar R$354,80.")
#             else: 
#                 if renda > 4600:
#                     print("Deve pagar R$869,36.")

# if modelo == 2:
#     if renda <= 2500:
#         print("Isento.")
#     else:
#         if renda < 3700:
#          print("Deve pagar R$187,54.")
#         else:
#             if renda < 6100:
#                 print("Deve pagar R$465,95.")
#             else: 
#                 if renda > 6100:
#                     print("Deve pagar R$1141,71.")

# if modelo == 3:
#     if renda <= 4700:
#         print("Isento.")
#     else:
#         if renda < 7000:
#          print("Deve pagar R$353,29.")
#         else:
#             if renda < 9200:
#                 print("Deve pagar R$877,78.")
#             else: 
#                 if renda > 9200:
#                     print("Deve pagar R$1573,80.")