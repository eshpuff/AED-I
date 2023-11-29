'''Crie uma lista de nomes de cidades. Peça ao usuário para digitar o nome de uma cidade e verifique se ela está presente na lista. Se estiver, remova a cidade da lista e imprima a lista resultante. Caso contrário, imprima uma mensagem dizendo que a cidade não foi encontrada. Faça 2 versões desse exercício, uma usando a função “remove” e outra sem usar funções prontas do python.'''

lista_cidades = ["Rio Grande", "Pelotas", "Porto Alegre", "Gramado", "São Paulo", "Rio de Janeiro", "Florianópolis", "Curitiba"]

cidade = input("Digite uma cidade: ")

if cidade in lista_cidades:
    lista_cidades.remove(cidade)
    print(lista_cidades)

else:
    print("Cidade não encontrada.")