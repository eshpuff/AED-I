'''Escreva um programa que leia diversos funcionários e seu respectivo salario, ate que o nome de um funcionário seja “fim”. 7
Em seguida escreva:
a) O nome do funcionário com maior salário
b) O nome do funcionário com menor salário
c) A média dos salários digitados'''

func_maior_salario = ""
func_menor_salario = ""
maior_salario = 0
menor_salario = 0
soma = 0
i = 0

funcionario = input("Insira o nome do funcionário (Ou 'Fim' para sair.): ")

while funcionario != "Fim":
    salario = float(input("Digite o salário do funcionário: "))
    if i == 0:
        maior_salario = salario
        menor_salario = salario
        func_maior_salario = funcionario
        func_menor_salario = funcionario
    
    else:
        if salario > maior_salario:
            maior_salario = salario
            func_maior_salario = funcionario
        if salario < menor_salario:
            menor_salario = salario
            func_menor_salario = funcionario
    
    soma += salario
    i += 1
    funcionario = input("Insira o nome do funcionário (Ou 'Fim' para sair.)")

if i > 0:
    media = soma / i
    print("O funcionário com maior salário é:",func_maior_salario)
    print("O funcionário com menor salário é:", func_menor_salario)
    print("A média dos salários é:", media)

else:
    print("Nenhum funcionário foi inserido.")
