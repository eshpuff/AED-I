'''Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um programa
que solicite esses dados (finalize a entrada de dados ao ser digitada uma idade negativa) e mostre:
a) A média dos salários do grupo;
b) A maior e a menor idade do grupo;
c) A quantidade de mulheres na região;
d) A idade e o sexo da pessoa que possui o maior salário.'''

mulher = 0
homem = 0
soma = 0
i = 0
idade = int(input("Insira a idade (Insira idade negativa para terminar): "))

maior_idade = 0
menor_idade = 0
maior_salario = 0
sexo_maior_salario = ""
idade_maior_salario = 0

while idade > 1:
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade    
    sexo = str(input("Qual o sexo (M ou F)? ").upper())
    if sexo == str("F"):
        mulher += 1
    else:
        homem += 1
    
    salario = int(input("Insira o salário: "))

    if salario > maior_salario:
            maior_salario = salario
            idade_maior_salario = idade
            sexo_maior_salario = sexo 
    
    soma += salario
    i += 1
    idade = int(input("Insira a idade (Insira idade negativa para terminar): "))
    
if i > 0:
    media = soma / i
    print("A média dos salários é:",media)
    print("A maior idade é:",maior_idade)
    print("A menor idade é:",menor_idade)
    print("A quantidade de mulheres na região é:",mulher)
    print("A idade da pessoa com maior salário é",idade_maior_salario,"e seu sexo é",sexo_maior_salario)