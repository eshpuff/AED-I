# 16) Uma universidade deseja fazer um levantamento a respeito de seu processo de seleção.
# Para cada curso, é fornecido um arquivo texto com o seguinte conjunto de valores:
# Nome do curso;
# Código do curso;
# Número de vagas;
# Número de candidatos do sexo masculino;
# Número de candidatos do sexo feminino
# Fazer um programa em Python que:
# • Calcule e escreva, para cada curso, o número de candidatos por vaga e a porcentagem de
# candidatos do sexo feminino (escreva também o código correspondente do curso);
# • Determine o maior número de candidatos por vaga e escreva esse número juntamente
# com o código do curso correspondente (supor que não haja empate);
# • Calcule e escreva o total de candidatos.

arq = open("ex16.txt", "r")
lines = arq.readlines()

temp = 0
tempId = ""
fullTotal = 0

for i in lines:
    text = i.split(";")
    total = int(text[3])+int(text[4])
    fullTotal += total
    percent = (int(text[4])*100)/int(total)
    print(f"O número de vagas de candidatos por vaga do curso {text[1]} é {total}, e a porcentagem feminina é de {percent:,.2f}%")
    candForVacancy = total/int(text[2])
    if candForVacancy > temp:
        tempId = text[1]
        temp = candForVacancy

print(f"O curso {tempId} possuí {str(temp)} candidatos por vaga")
print(f"O total de cadidatos é de {fullTotal}")
