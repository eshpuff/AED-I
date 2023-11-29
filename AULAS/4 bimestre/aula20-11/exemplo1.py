#função adicionar notas
# função calcular média
#fazer função consultarNotaAluno

def adicionarNotas(notas):
    nome = input("Insira o nome do aluno: ")
    nota = float(input("Insira sua nota: "))
    notas[nome] = nota
    return notas

def calcularMedia(notas):
    total = len(notas)
    soma = 0
    for pessoa in notas:
        soma += float(notas[pessoa])
    media = soma / total
    return media

def consultarNotaAluno(notas,nome):
    print(f"Nota de {nome}: {notas[nome]}")


notas = {'João' : 10,
'Maria' : 9.5}

notas = adicionarNotas(notas)

print(notas)
print("A média da turma:",calcularMedia(notas))

print(consultarNotaAluno(notas, 'João'))
