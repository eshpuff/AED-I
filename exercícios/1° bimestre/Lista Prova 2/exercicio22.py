'''Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos 
restantes. Faça um programa em Python que receba o nome do(a) ginasta, e as notas de sua apresentação dadas pelos sete jurados. Ao final, informe a melhor nota, 
a pior nota e a sua média final, conforme a descrição acima informada (ou seja, retirar a melhor e a pior nota para calcular a média). As notas não são informadas
em ordem (crescente ou decrescente).'''

ginasta = input("Isira nome do atleta: ")
notas = []
i = 1

while i <= 7:
    nota = float(input("Digite a nota do jurado "+i+": "))
    i += 1

m_nota =  notas