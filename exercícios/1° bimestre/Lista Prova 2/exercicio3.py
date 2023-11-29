'''Construa um programa em python que, informadas três medidas a, b e c pelo usuário, verifique se elas podem ser lados de um triângulo.
Se não puderem ser, primeiramente o algoritmo deve informar isso. Se for possível serem lados de triângulo, deve dizer qual tipo de 
triângulo pode ser construído com essas medidas (isósceles, escaleno ou equilátero). A condição para formar um triângulo: comprimento do 
maior segmento seja inferior à soma dos comprimentos dos dois menores.'''

a = float(input("Insira o valor do primeiro lado: "))
b = float(input("Insira o valor do segundo lado: "))
c = float(input("Insira o valor do terceiro lado: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("A figura é um triângulo ")
    if a == b == c:
        print("equilátero.")
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print("isóceles.")
    if a != b and b != c and c != a:
        print("escaleno.")

else:
    print("A figura não é triângulo.")