'''5) Faça uma função em Python para calcular X elevado à Y, ou X^Y. A função deverá receber, por parâmetro, X e Y, e retornar o resultado da chamada da subrotina. Exemplo: 2 elevado à
3 é igual à 2*2*2 = 8. Os parâmetros são 2 e 3, e o retorno será 8. Obs: implementar
exatamente como no exemplo, ou seja, a exponenciação deve ser calculada por
multiplicações sucessivas.'''

x = int(input("Insert your base number: "))
y = int(input("Insert your exponent number: "))

def calculating(x,y):
    if x == 0:
        print("Neutral base results 0 as a value.")

    elif y == 0:
        print("Neutral exponents results 1 as a value.")        

    else:
        mult = 1
        for _ in range(y):
            mult *= x
        print("The result is:", mult)
calculating(x,y)