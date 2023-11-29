gabarito = "HOLANDA"
pais = input("Qual o país? ").upper()
tentativa = 1

dica1 = "Um país da Europa."
dica2 = "A cor é laranja."
dica3 = "No passado invadiu o Brasil."
dica4 = "O idioma é o holandês."

while pais != gabarito and tentativa < 5:
    print("Errrrou!")
    if tentativa == 1:
        print(dica1)
    else:
        if tentativa == 2:
            print(dica2)
        else:
            if tentativa == 3:
                print(dica3)
            else:
                print(dica4)

    tentativa = tentativa + 1
    pais = input("Qual o país? ").upper()

if pais == gabarito:
    print("Finalmente acertou.")
else:
    print("Não conseguiu.")