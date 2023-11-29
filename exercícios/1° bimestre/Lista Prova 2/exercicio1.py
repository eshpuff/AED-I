'''Faça um programa que, ao receber os valores da largura e do comprimento de uma figura geométrica, mostre se esta é um quadrado 7
ou apenas um retângulo. Caso um valor seja menor ou igual a zero, deve-se mostrar um erro.'''

lado1 = float(input("Informe o Lado 1: "))
lado2 = float(input("Informe o Lado 2: "))

if (lado1 <=0 ) or (lado2 <= 0):
    print("Valor inválido. O lado deve ser maior que 0.")
else:
    if lado1 == lado2:
        print("A figura é um quadrado!")
    else:
        print("A figura é um retângulo!")