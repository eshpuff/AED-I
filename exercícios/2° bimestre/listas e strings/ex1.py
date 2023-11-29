''' Crie uma função em Python que verifique se a string informada por parâmetro é um número válido. Por exemplo: "12354" --> True "ABC123" --> False'''

string = input("Insira um número: ")
i = 0
numeros = ['1','2','3','4','5','6','7','8','9','0','.','-']
verdadeiro = 0

while i < len(string):
    if string[i] in numeros:
        verdadeiro += 1
    i += 1

if verdadeiro == len(string):
    print(string+" ---> True")
else:
    print(string+" ---> False")