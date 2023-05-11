 n=int(input("num:"))
 if n<0:
     n=n*-1
     print(n)
 else:
     print("O numero é:", n)


# #Leia a idade e diga se pode beber ou se não pode
 i=int(input("idade:"))
if i<18:
     print("Não pode beber.")
else:
     print("Pode beber.")


#Leia um número e diga se ele é par ou impar
 n=int(input("Informe o número:"))
 if n%2==0:
     print("O número é par.")
 else:
     print("O número é impar.")


#Leia a idade e diga sobre a votação
#menor de 16: não vota
#entre 16 e 18: voto facultativo
#entre 18 e 70: obrigatorio
#maior de 70: facultativo

 i=int(input("Insira a idade:"))
 if i<16:
     print("Não vota.")
 else:
     if i<18:
         print("Voto facultativo.")
     if (i>=18 and i<=70):
         print ("Voto obrigatório")
     if i>70:
         print("Voto facultativo")


 
 i=int(input("Insira sua idade:"))
 if i<16:
     print("Não vota.")
 else:
     if (i>=16 and i<18 or i>70):
         print ("Voto facultativo.")
     if (i>=18 and i<=70):
         prints ("voto obrigatório.")


#Ferias: custa menos de 30?
# #Tem pscina?
# Tem wifi?
# Tem local para fogueira e churrasco?

price=int(input("Qual valor?"))
if price>30:
    print("Não tem férias.")
else:
    churras= input("Tem churrasco?")
    if (churras== "sim"):
        print ("Tem férias.")
    else:
        pool= input("Tem psicina?")
        wifi= input("Tem wifi?")
        if (pool== "sim" and wifi== "não" or pool=="não" and wifi=="sim"):
            print("Não tem ferias")
        else: 
            print("Tem férias") 
