''' Faça um programa em Python que leia duas informações de N alunos: a primeira informação representa a matrícula do aluno, e a 
segunda é a sua altura em centímetros. Solicite inicialmente o valor N, e a seguir encontre o aluno mais alto e o mais baixo dessa
classe. Ao final, apresente as matrículas do aluno mais alto e do aluno mais baixo, junto com suas respectivas alturas.'''

n = int(input("Insira quantidade de alunos: "))

aluno_alto = ""
mais_alto = 0
aluno_baixo = ""
mais_baixo = float("inf")

i = 1

while i <= n:
    matricula = input("Digite a matrícula do aluno {}: ".format(i))
    altura = float(input("Digite a altura do aluno {} em centímetros: ".format(i)))

    if altura > mais_alto:
        aluno_alto = matricula
        mais_alto = altura

    if altura < mais_baixo:
        aluno_baixo = matricula
        mais_baixo = altura

    i += 1

print("Aluno mais alto:")
print("Matrícula:", aluno_alto)
print("Altura:", mais_alto, "cm")

print("Aluno mais baixo:")
print("Matrícula:", aluno_baixo)
print("Altura:", mais_baixo, "cm")