def step(x, value):
    x = x + value
    print("2º print - Endereço de x:", id(x))
    cont = 0
    print("1º print - Endereço de cont:", id(cont))
    while cont < 10:
        cont += 1
        print("3º print - Endereço de cont:", id(cont))

step(0, 1)