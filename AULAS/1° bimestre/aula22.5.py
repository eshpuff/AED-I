''' montar algoritmo onde se le a data e então diz se é valido ou não'''

dia= int(input("Insira o dia: "))
mes= int(input("Insira o mês: "))
ano= int(input("Insira o ano: "))
bi= ano%4

if mes > 12 or mes <1:
    print("Mes inválido.")

if dia > 31 or dia < 1:
    print("Dia inválido 1.")

else:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia > 31:
                print("Dia inválido 2.")
        if mes != 1 or mes != 3 or mes != 5 or mes != 7 or mes != 8 or mes != 10 or mes != 12:
            if dia > 30:
                print("Dia inválido 3.")
        if mes == 2 and dia > 29:
            print ("Dia inválido 4.")
        if (mes == 2 and bi != 0):
            if dia > 28:
                print("Dia Inválido.")
        else:
            print("Data válida.")
          
''' Descobrir o país '''
pais= "JAPÃO"
tentativa= input("Informe um país: ").upper()

while tentativa != pais:
    print("Errou! 😓")
    tentativa= input("Informe um país: ").upper()

print("Acertou 🤩. O país é "+tentativa)

''' Descobrir o país com 5 tentativas '''
pais= "BRASIL"
i= 1
tentativa= input("Informe um país: ").upper()

if (tentativa == pais):
   print("Acertou 🤩. O país é "+tentativa)

else:
   while tentativa != pais and i < 5:
       print("Errou! Foram ",i," tentativas.")
       tentativa= input("Informe um país: ").upper()
       i = i + 1

       if (tentativa == pais):
           print("Acertou 🤩. O país é "+tentativa)
       if i == 5:
           print("Acabaram suas tentativas.")

'''Descobrir o país Holanda com 5 tentativas a cada tentativa uma dica'''
pais= "HOLANDA"
i= 1
tentativa= input("Informe um país: ").upper()

if (tentativa == pais):
    print("ACERTOU!")

else:
    while tentativa != pais and i < 5:
        print("ERRRRROU!")
        if i == 1:
            print("Dica: É um país da Europa.")
            if (tentativa == pais):
                print("ACERTOU!")
            
            else:    
                tentativa= input("Informe um país: ").upper()
                i = i + 1

        if i == 2:
            print("Dica: No passado invadiu o Brasil.")
            if (tentativa == pais):
                print("ACERTOU!")
        tentativa= input("Informe um país: ").upper()
        i = i + 1

        if i == 3:
            print("Dica: Era das flores e dos moinhos de vento.")
            if (tentativa == pais):
                print("ACERTOU!")
        tentativa= input("Informe um país: ").upper()
        i = i + 1

        if i == 4:
            print("Dica: Na final da copa perdeu para espanha.")
            if (tentativa == pais):
                print("ACERTOU!")
        tentativa= input("Informe um país: ").upper()
        i = i + 1

        if i == 5:
            print("Dica: Seu idioma é o holandes.")
            if (tentativa == pais):
                print("ACERTOU!")
        tentativa= input("Informe um país: ").upper()
        i = i + 1
      
''' loop com contador '''
i =  1
while i <= 1000:
    print(i,str(" Eu amo AED1 😍."))
    i = i + 1
