'''Faça um programa em Python que solicite a idade de N pessoas. Ao final, o programa deverá verificar se a média de idade da turma 
varia entre 0 e 25, 26 e 60 ou maior que 60, informando se a turma é jovem, adulta ou idosa, conforme a média calculada. Mas será que
a idade média da turma é uma boa métrica? Qual alternativa para melhor verificar qual grupo dominante? Implemente uma possível 
alternativa.'''

idade = int(input("Infora a idade (Insira um número negativo para parar): "))
i = 0
soma = 0

while idade >= 0:
    i += 1
    soma = soma + idade
    idade = int(input("Infora a idade (Insira um número negativo para parar): "))

media = soma / i

if media > 0 and media < 25:
    print("A população é jovem.")
if media > 26 and media < 60:
    print("A população é adulta.")
if media > 60:
    print("A popualação é idosa.")



'''idade = int(input("Insira sua idade (Insira número negativo para parar): "))
jovem = 0
adulta = 0
idosa = 0
i = 0
soma = 0

while idade > 0:
    if idade < 25:
        jovem += 1
    else:
        if idade < 59:
            adulta += 1
        else:
            if idade > 60:
                idosa += 1
    i += 1
    idade = int(input("Insira a idade (Insira número negativo para parar): "))


if jovem > adulta and jovem > idosa:
    print("A população é jovem.")
if adulta > jovem and adulta > idosa:
    print("A população é adulta.")
if idosa > jovem and idosa > adulta:
    print("A população é idosa.")'''